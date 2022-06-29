.. _pl4A7fhPns:

=======================================
NIX/User Mgt
=======================================

.. code-block:: console

    $ sudo adduser <user name>

    $ sudo usermod -aG dialout <user name>      # access to serial ports
    $ sudo usermod -aG docker <user name>       # access to docker daemon
    $ sudo usermod -aG sudo <user name>
