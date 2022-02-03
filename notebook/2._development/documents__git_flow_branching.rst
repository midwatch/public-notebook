.. _3s-SVAibUn:

=======================================
Git Flow Branching Model
=======================================

Quick steps for using branching models as laid out in [1].

Some repositories, such as <redacted>-module, contain support branches for longterm
maintenance of legacy code/systems. (ex: support-1.x)

Development automation via invoke using standard task library[2].

Merge Updates into Current Branch
---------------------------------------------------------------------------------------------------

From a content prespective, rebasing is changing the base of your branch from one commit to another
making it appear as if you'd created your branch from a different commit.

The primary reason for rebasing is to maintain a linear project history.

See [3].

.. code-block:: console

    $ git rebase

References
---------------------------------------------------------------------------------------------------
#. `A Successful Git Branching Model <http://nvie.com/posts/a-successful-git-branching-model/>`_
#. `Invoke Task Library <https://github.com/stout762/py-invoke-lib>`_
#. `git rebase <https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase>`_
#. `PDF Version of main figure <http://nvie.com/files/Git-branching-model.pdf>`_
#. `Git-flow Cheatsheet <https://danielkummer.github.io/git-flow-cheatsheet/>`_

.. image:: _include/images/git-model.png

