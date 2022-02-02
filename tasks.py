from pathlib import Path

from invoke import Collection
from invoke import task
from invoke.exceptions import Failure

GITHUB_USERNAME = "midwatch"
GITHUB_SLUG = "public-notebook"
CC_VERSION = "0.0.0"

RSYNC_HOST = "host"
RSYNC_USER = "user"
RSYNC_PATH_LOCAL = "build/www/"
RSYNC_PATH_REMOTE = "remote path"

TEMPLATE_ROOT = "project.d/templates"
TEMPLATE_NAME = "index_table.rst.jinja"

ROOT_DIR = Path(__file__).parent


@task
def clean_build(ctx):
    """
    Clean up files from package building
    """
    ctx.run("rm -fr build/")


@task
def scm_init(ctx):
    """Init scm repo (if required).

    Raises:
        Failure: .gitignore does not exist

    Returns:
        None
    """
    if not Path('.gitignore').is_file():
        raise Failure('.gitignore does not exist')

    if not Path('.git').is_dir():
        uri_remote = 'git@github.com:{}/{}.git'.format(GITHUB_USERNAME,
                                                       GITHUB_SLUG
                                                      )

        ctx.run('git init')
        ctx.run('git add .')
        ctx.run('git commit -m "new package from midwatch/cc-py3-pkg ({})"'.format(CC_VERSION))
        ctx.run('git branch -M main')
        ctx.run('git remote add origin {}'.format(uri_remote))
        ctx.run('git tag -a "v_0.0.0" -m "cookiecutter ref"')


@task
def scm_push(ctx):
    """Push all branches and tags to origin."""

    for branch in ('develop', 'main'):
        ctx.run('git push origin {}'.format(branch))

    ctx.run('git push --tags')


@task
def scm_status(ctx):
    """Show status of remote branches."""
    ctx.run('git for-each-ref --format="%(refname:short) %(upstream:track)" refs/heads')


@task(pre=[clean_build])
def clean(ctx):
    """
    Runs all clean sub-tasks
    """
    pass


@task(clean)
def build(ctx):
    """
    Build html pages.
    """
    notebook_opts = (
        f'--template-dir {TEMPLATE_ROOT}',
        f'--template-name {TEMPLATE_NAME}',
        'notebook/',
        'build/rst/index.rst'
        )

    ctx.run('mkdir build')
    ctx.run('cp -r notebook build/rst')
    ctx.run('sphinx_notebook build {}'.format(' '.join(notebook_opts)))
    ctx.run('sphinx-build -b html build/rst build/www')


@task
def new(ctx, template, path):
    """
    Add a new note from a template.
    """
    # template = template + '.rst.jinja'

    opts = (
        f'--template-dir {TEMPLATE_ROOT}',
        f'--template-name {template}.rst.jinja',
        path
        )

    # ctx.run(f'sphinx_notebook new note --template-dir {TEMPLATE_ROOT} --template-name {template} {path}')
    ctx.run('sphinx_notebook new note {}'.format(' '.join(opts)))

@task
def init(ctx):
    """Initialize freshly cloned repo"""
    scm_init(ctx)

    ctx.run('git flow init -d')
    ctx.run('git flow config set versiontagprefix v_')

    scm_push(ctx)


@task(pre=[clean, build])
def release(ctx):
    """
    Make a release of the python package to pypi
    """
    # ctx.run(f'rsync -r --delete {RSYNC_PATH_LOCAL} {RSYNC_USER}@{RSYNC_HOST}:{RSYNC_PATH_REMOTE}')

scm = Collection()
scm.add_task(scm_push, name="push")
scm.add_task(scm_status, name="status")

ns = Collection(build, clean, init, new, release)
ns.add_collection(scm, name="scm")
