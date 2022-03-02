.. _nrcF4K9ICf:

=======================================
New Release
=======================================

Prerequisites
=======================================

* Actionable:

  * use case(s)
  * bugs
  * documentation updates


Tasks
=======================================

Plan Release
---------------------------------------

#. Create new release project on Github
#. Assign Github issues to project


Implement Features
---------------------------------------

Move issue card to *In Progress* on project board

.. code-block:: console

    $ git flow feature start {issue id}_{friendly name}


* write failing test(s)
* implement feature


.. code-block:: console

    $ inv test
    $ inv format
    $ inv lint
    $ inv test
    $ git flow feature finish {issue id}_{friendly name}
    $ inv scm.push

Move issue card to *Complete* on project board and close


Release
---------------------------------------

.. code-block:: console

    $ inv test
    $ inv lint

    $ git flow release start x.y.0
    $ inv bumpversion {major,minor}


Update:

* README.rst
* CHANGELOG.rst

.. code-block:: console

    $ inv release
    $ git flow release finish x.y.0
    $ inv scm.push

Close Github project


Common Errors & Ommisions
=======================================

#. TBD


References
=======================================

#. TBD
