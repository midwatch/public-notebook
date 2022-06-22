.. _Q7HygZJbuR:

=======================================
New Solution
=======================================

Prerequisites
=======================================

* Actionable use case(s)
* Github account
* Github repo name
* Optional

  * PyPi account
  * PyPi package name


Tasks
=======================================

Bootstrap Repo
---------------------------------------

* Create new public or private repo on Github

.. code-block:: console

    $ cd ~/dev
    $ cookiecutter gh:{user}/{repo-name}
    $ cd {github-slug}
    $ vagrant up
    $ vagrant reload
    $ vagrant ssh
    $ cd /vagrant
    $ inv init


**Standard Cookie Cutters:**

.. list-table::
   :header-rows: 1

   * - Name
     - Repo
     - Comments
   * - midwatch/cc-py3-pkg
     - `Github <https://github.com/midwatch/cc-py3-pkg>`_
     - Python 3 CLI application


Verify Tool Chain
---------------------------------------

Release and install an absoulte minimal solution to prove release tool chain.

**Inital Release:**

.. code-block:: console

    $ git flow release start 0.1.0
    $ inv bumpversion minor
    $ inv release
    $ git flow release finish 0.1.0
    $ inv scm.push


**Test Install:**

In a new terminal:

.. code-block:: console

    $ cd ~/dev/dev-test-box
    $ vagrant destroy --force
    $ vagrant up
    $ vagrant reload
    $ vagrant ssh
    $ pipx install {PyPi Package Name}


Common Errors & Ommisions
=======================================

#. TBD


References
=======================================

#. TBD
