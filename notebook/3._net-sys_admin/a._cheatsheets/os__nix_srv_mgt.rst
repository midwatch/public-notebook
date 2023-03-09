.. _9uWSdLb04v:

=======================================
Linux/Service Mgt
=======================================

OpenRC
=======================================

.. code-block:: console

    $ rc-update add <service> <runlevel>
    $ rc-update del <service> <runlevel>
    $ rc-service <service> <start stop restart>

    $ rc-status
    $ rc <runlevel>

    $ reboot
    $ halt      # Equivalent to shutdown -r now
    $ poweroff  # Equivalent to shutdown -h now


**Notes:**

#. Runlevels: default, hotplugged, manual

**Service Files:**

* /etc/conf.d
* /etc/init.d

**References:**

#. `OpenRC Homepage <https://wiki.gentoo.org/wiki/OpenRC>`_
#. `OpenRC Service Script Writing Guide <https://github.com/OpenRC/openrc/blob/master/service-script-guide.md>`_


SystemD
=======================================

.. code-block:: console

    $ systemctl start <service>
    $ systemctl stop <service>
    $ systemctl enable <service>
    $ systemctl disenable <service>
    $ systemctl is-enabled <service>
    $ systemctl daemon-reload                           # Use when you create or modify a service file
    $ systemctl list-unit-files | grep enabled          # List all enabled services


**Service Files:**

* /etc/systemd/system
* /etc/systemd/user

**References:**

#. `Systemd For Upstart Users <https://wiki.ubuntu.com/SystemdForUpstartUsers>`_
