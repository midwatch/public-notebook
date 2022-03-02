.. _N6CPHoNb25:

=======================================
Vagrant
=======================================

.. code-block:: console

    $ vagrant init <box image>      - Create new Vagrant file with <box image>
    $ vagrant up
    $ vagrant status
    $ vagrant halt

    $ vagrant destroy

        options:

            -f, --force             - Destroy without confirmation

    $ vagrant global-status         - List status of all known Vagrant environments

    $ vagrant global-status | grep running


**Notes:**

* Have to configure port forwarding in Vagrant file to expose any internal ports
 * EX: config.vm.network "forwarded_port", guest: 8080, host: 8080

* Running servers inside of vagrant must be bound to all IP addresses so they'll be reachable from the host
 * EX: dev_appserver.py --host 0.0.0.0 app.yaml


Standard Boxes
=======================================

Alpine
---------------------------------------

 .. list-table::
    :header-rows: 1

    * - Box/Image Name
      - Source URL
      - Comments
    * - alpine/alpine64
      - `Vagrant Cloud <https://app.vagrantup.com/alpine/boxes/alpine64>`_
      - Alpine 3.7.0

Debian
---------------------------------------

 .. list-table::
    :header-rows: 1

    * - Box/Image Name
      - Source URL
      - Comments
    * - debian/stretch64
      - `Vagrant Cloud <https://app.vagrantup.com/debian/boxes/stretch64>`_
      - Debian 9
    * - debian/jessie64
      - `Vagrant Cloud <https://app.vagrantup.com/debian/boxes/jessie64>`_
      - Debian 8


Ubuntu
---------------------------------------

 .. list-table::
    :header-rows: 1

    * - Box/Image Name
      - Source URL
      - Comments
    * - ubuntu/focal64
      - `Vagrant Cloud <https://app.vagrantup.com/ubuntu/boxes/focal64>`_
      - Ubuntu 20.04 LTS
    * - ubuntu/bionic64
      - `Vagrant Cloud <https://app.vagrantup.com/ubuntu/boxes/bionic64>`_
      - Ubuntu 18.04 LTS
    * - ubuntu/xenial64
      - `Vagrant Cloud <https://app.vagrantup.com/ubuntu/boxes/xenial64>`_
      - Ubuntu 16.04 LTS
    * - ubuntu/trusty64
      - `Vagrant Cloud <https://app.vagrantup.com/ubuntu/boxes/trusty64>`_
      - Ubuntu 14.04 LTS



References
=======================================

#. TBD
