.. _AOEsZqPAz0:

=======================================
NIX Net File Systems
=======================================

CIFS/SMB
=======================================

.. code-block:: console

    $ sudo mount -t cifs //<host_name>/<volume name> \
        /mnt/<mount point> -o username=<username>,password=<password>

**Notes:**

* requires samba-common (debian/ubuntu)


NFS
=======================================

.. code-block:: console

    $ sudo mount -t nfs <server_ip>:/share_name \   - options (-o) sync|async
        /mnt/<mount point>

    $ showmount -e <server ip>                      - Export list for <server>

**Notes:**

* Requires nfs-common (debian/ubuntu)
