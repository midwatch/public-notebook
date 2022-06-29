.. _k9-utrQ387:

=======================================
Devpi
=======================================

.. code-block:: console

    $ devpi use http://devpi:4040
    $ devpi login <username>

    $ devpi user -c packages  \                         # Create user
            email=packaging@company.com \
            password=<password>

    $ devpi user -l                                     # List users

    # Create Package Indexes
    $ devpi index -c packages/stable \                  # [1]
            bases=root/pypi \
            volatile=False

    $ devpi index -c packages/staging \                 # [2]
            bases=packages/stable \
            volatile=True

    $ devpi index -c packages/develop \                 # [3]
            bases=packages/stable \
            volatile=True

    # Build and upload packages
    $ cd ~/dev/simpy
    $ python3 setup.py sdist bdist_wheel
    $ twine upload -r devpi-stable dist/*

    # Redirect pip to use a devpi index instead of pypi
    $ devpi use devpi-{stable,staging,develop}

**Notes:**

#. Our private stable packages and the pypi package cache
#. Our testing packages (eg: release/x.y.z)
#. Develop builds

Package Indexes:
=======================================

* root/pyi:
    * The Pypi repository

* packages/stable:
    * Inherits from root/pypi
    * Our private/internal packages (eg propriatry pypi)
    * volatile=False

* packages/staging:
    * Inherits from packages/stable (and thus root/pypi)
    * volatile=True allows destructive actions on the index (like overriding or deleting
      packages)

* packages/develop:
    * Inherits from packages/stable (and thus root/pypi)
    * volatile=True allows destructive actions on the index (like overriding or deleting
      packages)

pip.conf
=======================================

File Location:

* ~/.config/pip/pip.conf (unix default)
* ~/.pip/pip.conf (legacy)

In our system we store a common pip.conf for use in our development vms and
that file is copied to the vm during the provision process the following in the
Vagrantfile

config.vm.provision "file", source: "~/dev/.config/pip.conf", destination: "/home/vagrant/.config/pip/pip.conf"


.. code-block:: ini

    [global]
    index-url = http://devpi:4040/packages/stable

    [distutils]
    index-servers =
        devpi-stable
        devpi-staging
        devpi-develop

    [devpi-stable]
    repository = http://devpi:4040/packages/stable
    username = packages

    [devpi-staging]
    repository = https://devpi:4040/packages/staging
    username = packages

    [devpi-develop]
    repository = https://devpi:4040/packages/develop
    username = packages


Management
=======================================

The devpi server is managed directly from the host server because the devpi
management commands are intentionally broken/disabled in Nginx.

.. code-block:: console

    $ ssh <user>@<server>
    $ devpi use http://localhost:3141
    $ devpi login <username>

    $ devpi index --list

    # Show index configuration
    $ devpi getjson http://localhost:3141/packages/develop


References
=======================================

#. `Devpi Workflow <https://gist.github.com/christopherdcunha/3a4eaced12424bf58b6d>`_
#. `Getting started with devpi <https://stefan.sofa-rockers.org/2017/11/09/getting-started-with-devpi/>`_
#. `PIP Config file <http://pip.readthedocs.io/en/stable/user_guide/#config-file>`_
#. `Devpi User Manual <https://devpi.net/docs/devpi/devpi/latest/+d/userman/index.html>`_
