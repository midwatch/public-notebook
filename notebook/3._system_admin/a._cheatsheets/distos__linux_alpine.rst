.. _2c8mo5hnAo:

=======================================
Linux - Alpine
=======================================

Installation
=======================================

Management
=======================================

Packages
---------------------------------------

Basic Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    $ apk update
    $ apk upgrade
    $ apk add <package 1> <package 2>
    $ apk del <package 1> <package 2>

    # Find Packages
    $ apk search -v
    $ apk search -v 'acf*'
    $ apk search -v --description 'NTP'

    # Install Packages From Pinned Repos
    $ apk add stableapp newapp@edge bleedingapp@testing

    # Add A Local Package
    $ apk add --allow-untrusted /path/to/file.apk

    # Install From Repos Not In /etc/apk/repositories
    $ apk add cherokee --update-cache \
                       --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \
                       --allow-untrusted

    # Save Changes
    $ lbu commit -d

Notes:

#. Alpine running in ram disk mode does not restore packages installed from repos not in
   /etc/apk/repositories

Services
---------------------------------------

Alpine uses the OpenRC init system

.. code-block:: console

    $ rc-update add <service> <runlevel>
    $ rc-update del <service> <runlevel>
    $ rc-service <service> <start stop restart>

    $ rc-status
    $ rc <runlevel>

    $ reboot
    $ halt      # Equivalent to shutdown -r now
    $ poweroff  # Equivalent to shutdown -h now

Notes:

#. Runlevels: default, hotplugged, manual

Service Files:

* /etc/conf.d
* /etc/init.d

Resources
=======================================

#. `Alpine Wiki <https://wiki.alpinelinux.org/wiki/Main_Page>`_
#. `Alpine Package Repo <http://dl-cdn.alpinelinux.org/alpine/>`_

References
=======================================

#. `Alpine Package Management <https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>`_
#. `Alpine Local Backup <https://wiki.alpinelinux.org/wiki/Alpine_local_backup>`_
#. `Alpine Linux Init System <https://wiki.alpinelinux.org/wiki/Alpine_Linux_Init_System>`_
#. `OpenRC Service Script Writing Guide <https://github.com/OpenRC/openrc/blob/master/service-script-guide.md>`_
