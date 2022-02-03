.. _ld4uN6s4Ki:

=======================================
Rsync
=======================================

Basic Syntax
=======================================

.. code-block:: console

    $ rsync options source destination

    Options:
        -a          archive mode            (recursive + preserves symbolic links,
                                             file permissions, user & group
                                             ownership, and timestamps)

        -h          human-readable
        -r          recursive               (doesn't perserve timestamps and
                                             permissions)

        -v          verbose
        -z          compress file data

        --dry-run
        --progress  show progress while transfering data

Copy/Sync Locally
=======================================

Sync backup.tar to /tmp/backups/

.. code-block:: console

    $ rsync -zvh backup.tar /tmp/backups


Sync all of the files from one directory to another on the local machine

.. code-block:: console

    $ rsync -avzh /root/rpmpkgs /tmp/backups

Copy/Sync Remotely
=======================================

Sync a file from a remote server

.. code-block:: console

    $ rsync -avzhe ssh <user>@<ip addr>:/root/install.log /tmp/

Sync a file to a remote server

.. code-block:: console

    $ rsync -avzhe ssh backup.tar <user>@<ip addr>:/backups/

Sync a directory to a remote server

.. code-block:: console

    $ rsync -avzhe ssh /my_dir/ <user>@$<ip addr>:/root/my_dir/

Include & Exclude
=======================================

Only transfer files and directories that start with 'R'

.. code-block:: console

    $ rsync -avzhe ssh --include 'R*' --exclude '*' <user>@<ip addr>:/root/install.log /tmp/

Delete
=======================================

Delete files at destination that are not in source

.. code-block:: console

    $ rsync -avz --delete <source> <destination>

Delete source files after successfull transfer

.. code-block:: console

    $ rsync -avz --remove-source-files <source> <destination>

References
=======================================

#. `10 Rsync Command Examples <https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/>`_.
