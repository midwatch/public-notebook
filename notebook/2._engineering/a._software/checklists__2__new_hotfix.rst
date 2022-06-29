.. _jyPPq3RUWW:

=======================================
New Hotfix
=======================================

Prerequisites
=======================================

* Application breaking bug
* Major documentation error


Tasks
=======================================

.. code-block:: console

    $ inv scm.pull
    $ git flow hotfix start x.y.z
    $ inv bumpversion patch

* Root cause analysis
* Write failing regression test
* Implement fix
* Update CHANGELOG.rst

.. code-block:: console

    $ inv test
    $ inv format
    $ inv lint
    $ inv test
    $ inv release
    $ git flow release finish x.y.z
    $ inv scm.push

* Close issue


Common Errors & Ommisions
=======================================

#. TBD


References
=======================================

#. TBD
