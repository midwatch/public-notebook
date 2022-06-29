.. _RlJ6sXZGL1:

=======================================
Environment
=======================================

Our standard development environment(s) and tooling.

Target Environment
=======================================

* Ubuntu/Kubuntu 20.04 LTS
* Python 3.8
* PipX


Dependencies
=======================================


External
---------------------------------------

* github_
* pypi_
* test-pypi_ (optional)

.. _github: https://github.com/
.. _pypi: https://pypi.org/
.. _test-pypi: https://test.pypi.org/


Host
---------------------------------------

* kubuntu 20.04 LTS
* python 3.8
* `Sublime Text <https://www.sublimetext.com/>`_
* virtualbox_
* git_
* vagrant_
* python-pip_
* python-pipx_
* python-cookiecutter_

.. _virtualbox: https://www.virtualbox.org/wiki/Documentation
.. _git: https://git-scm.com/doc
.. _vagrant: https://www.vagrantup.com/
.. _python-pip: https://pypi.org/project/pip/
.. _python-pipx: https://pypa.github.io/pipx/
.. _python-cookiecutter: https://cookiecutter.readthedocs.io/en/latest/

Config Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* $HOME/.gitconfig
* $HOME/.cookiecutterrc
* $HOME/.config/pip/pypi-token.sh


Appendices
=======================================

Configuration Files
---------------------------------------

.gitconfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    [user]
        email = user@example.com
        name = First Last


.cookiecutterrc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    default_context:
        full_name: "First Last"
        email: "user@example.com"
        github_username: "github user name"
    abbreviations:
        pp: https://github.com/audreyr/cookiecutter-pypackage.git
        gh: https://github.com/{0}.git
        bb: https://bitbucket.org/{0}

`Cookie Cutter User Config <https://cookiecutter.readthedocs.io/en/latest/advanced/user_config.html>`_


pypi-token.sh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    export POETRY_PYPI_TOKEN_PYPI=<pypi token>

`PyPI upload via API token <https://blog.python.org/2019/07/pypi-now-supports-uploading-via-api.html>`_
