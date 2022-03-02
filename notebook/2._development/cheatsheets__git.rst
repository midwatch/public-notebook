.. _3NaHEB71H6:

=======================================
Git
=======================================

.. code-block:: console

    $ git branch                        - List local branches

        options:

            -a, --all                   - List local and remote-tracking branches
            -d, --delete
            -D                          - Shortcut for --delete --force
            -r, --remotes               - List remote branches

    $ git checkout <branch>

        options:

            -b <new_branch>

    $ git log

    $ git ls-tree <branch>

    $ git pull

        options:

            --all                       - Pull all remote branches

    $ git rm

        options:

            --cached [filenames]        - Unstage and remove paths from index. Working tree files
                                          will be left alone.

            -n, --dry-rune

    $ git tag

        options:

            -a, --annotate
            -l <pattern, --list <pattern>


.. code-block:: console

    # Show Default Branch
    # -----------------------------------------------------------------------------------
    $ git remote show origin | grep 'HEAD branch' | cut -d' ' -f5


    # Checkout tags as a new branch
    # -----------------------------------------------------------------------------------
    $ git checkout -b v_x_y_x v_x_y_x


    # List the remote tracking info for each remote branch
    # -----------------------------------------------------------------------------------
    $ git for-each-ref --format="%(refname:short) %(upstream:track)" refs/heads


    $ git checkout <file>               - Throw away any changes to file


**Notes:**

#. Git doens't normally pull remote branches until you ask for them via git checkout
#. Show default branch useful to determine if repo has migrated to using main instead of master


References
=======================================

#. `GIT cheatsheet <https://education.github.com/git-cheat-sheet-education.pdf>`_
