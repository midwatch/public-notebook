.. _QQKO0h5RXx:

=======================================
Linux - Debian
=======================================

Releases
=======================================

Debian
---------------------------------------

 .. list-table::
    :header-rows: 1

    * - Version
      - Code Name
    * - 9
      - Stretch
    * - 8
      - Jessie
    * - 7
      - Wheezy
    * - 6
      - Squeeze

Ubuntu
---------------------------------------

 .. list-table::
    :header-rows: 1

    * - Version
      - Code Name
      - Short Name
    * - 20.04 LTS
      - Focal Fossa
      - focal
    * - 18.04 LTS
      - Bionic Beaver
      - bionic
    * - 16.04 LTS
      - Xenial Xerus
      - xenial
    * - 14.04 LTS
      - Trusty Tahr
      - trusty


Installation
=======================================

Management
=======================================

Packages
---------------------------------------


Basic Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    $ apt autoremove                              # remove unneeded auto-installed packages

    $ apt list                                    # display a list of packages satisfying certain criteria.
                                                  # similar to dpkg-query --list
    $ apt list python3

      Listing... Done
      python3/focal,now 3.8.2-0ubuntu2 amd64 [installed,automatic]
      python3/focal 3.8.2-0ubuntu2 i386

    $ apt list --installed

    $ apt list --installed python3

      Listing... Done
      python3/focal,now 3.8.2-0ubuntu2 amd64 [installed,automatic]

    $ apt list --installed not-installed-pkg

      Listing... Done


Snap: Snaps are app packages for desktop, cloud and IoT that are easy to
install, secure, cross‐platform and dependency‐free.


.. code-block:: console

  $ sudo snap remove obs-studio


Services
---------------------------------------

SystemD

.. code-block:: console

    $ systemctl start <service>
    $ systemctl stop <service>
    $ systemctl enable <service>
    $ systemctl disenable <service>
    $ systemctl is-enabled <service>
    $ systemctl daemon-reload                           # Use when you create or modify a service file
    $ systemctl list-unit-files | grep enabled          # List all enabled services

Service Files:

* /etc/systemd/system
* /etc/systemd/user


References
=======================================

#. `Systemd For Upstart Users <https://wiki.ubuntu.com/SystemdForUpstartUsers>`_
#. `How to remove a snap package on Ubuntu <https://linuxhint.com/remove-snap-package-ubuntu/>`_
