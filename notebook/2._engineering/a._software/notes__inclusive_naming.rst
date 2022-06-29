.. _03fO6QOHgt:

=======================================
Inclusive Naming
=======================================

Word Replacement List
=======================================

Master
---------------------------------------

* main
* control plane
* original
* source
* trunk


Master, Slave
---------------------------------------

* Control plane/control plane node
* Controller/doer
* Primary/replica
* Primary/secondary
* Leader/follower
* Parent/child


Whitelist, BlackList
---------------------------------------

* allowlist/denylist
* allowlist/blocklist
* allowedNoned/deniedNouns
* allow/block


Git
=======================================

Git Init Repo
---------------------------------------

**Git > 2.28:**

.. code-block:: console

    $ mkdir ~/.git-template
    $ echo "ref: refs/heads/main" > ~/.git-template/HEAD
    $ git config --global init.templateDir ~/.git-template
    $ git init

**Git <= 2.28:**

.. code-block:: console

    $ git config --global init.defaultBranch main
    $ git init


GitHub Migration
---------------------------------------

GitHub now defaults to main for the default branch when creating new repositories.

**Change/migrate existing repo's default branch:**

#. Navigate to repo's main page
#. Click on branches above file list
#. Click the pencil icon to the right of the master branch
#. Enter main
#. Click Rename branch

**Update a local clone after master branch has been renamed:**

.. code-block:: console

    $ git branch -m master main
    $ git fetch origin
    $ git branch -u origin/main main


References
=======================================

#. `Inclusive Naming Initiative <https://inclusivenaming.org/>`_
#. `INI Word List <https://inclusivenaming.org/language/word-list/>`_
#. `IETF Knodel Terminology <https://tools.ietf.org/id/draft-knodel-terminology-00.html#rfc.section.1.1>`_
#. `GitHub Rename Master Branch <https://github.com/github/renaming>`_
#. `Make git default to main <https://medium.com/dataseries/how-to-make-your-git-repos-default-to-main-instead-of-master-28b7a9d3d631>`_
