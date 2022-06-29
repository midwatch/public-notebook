.. _YTDJ86nP3w:

=======================================
Xen
=======================================

Manage Domains
=======================================

.. code-block:: console

    $ sudo xl console <host name>                       # <CTRL> ']' to detach
    $ sudo xl create /etc/xen/<host name>.cfg -c        # Boot guest domain [1]
    $ sudo xl list
    $ sudo xl shutdown <host name>

Notes:

#. -c attach console as soon as machine starts

Build New Guest
=======================================

.. code-block:: console

    $ sudo xen-create-image --mac 20:00:00:00:00:XX \
                            --hostname <host name> \
                            --password <password>

        Options:
                            --accounts                      # Copy all non-system accounts to guest system
                            --boot                          # Boot after creating
                            --force                         # Force overwriting existing images
                            --password=<passphrase>         # Set root password for new guestq
        Defaults:
            lvm             = xen-a-vg
            install-method  = debootstrap
            size            = 50G
            memory          = 2048M
            swap            = 2048M
            fs              = ext3
            dist            = ubuntu/xenial                 # Dom0 Distro
            image           = sparse
            dhcp            = 1
            bridge          = xenbr0
            passwd          = 0                             # Prompt for root password
            accounts        = 1                             # Copy host accounts to guest
            arch            = amd64
            apt-proxy       = http://apt-cache.rled-shop.lan:3142

    # Configure Normal User
    $ adduser <username>
    $ usermod -aG sudo <username>
    $ usermod -aG docker <username>                 # If using docker
    $ ssh-copy-id -i ~/.ssh/<key> <user>@<host>

Notes:

#. Take about 6 minutes to build a new image
#. Config files (hostname.cfg) saved in /etc/xen

Delete Guest
=======================================

.. code-block:: console

    # Delete Disk Image
    $ sudo lvremove /dev/xen-a-vg/<host name>-disk
    $ sudo lvremove /dev/xen-a-vg/<host name>-swap

    # Delete Config
    $ sudo rm /etc/xen/<host name>.cfg

References
=======================================

#. `Build Xen Guest using Xen-Tools <https://www.virtuatopia.com/index.php/Building_a_Xen_Guest_Domain_using_Xen-Tools>`_
#. `Xen Tools <https://blog.xenproject.org/2012/08/31/xen-tools-a-straightforward-vm-provisioninginstallation-tool/>`_
