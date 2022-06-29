.. _2Sg7VP8aSs:

=======================================
NIX/Package Mgt
=======================================

APK
=======================================

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

**Notes:**

#. Alpine running in ram disk mode does not restore packages installed from repos not in
   /etc/apk/repositories



APT
=======================================

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


Nala
---------------------------------------

Nala is a front-end for libapt-pkg. Specifically we interface using the
python-apt api.

Especially for newer users it can be hard to understand what apt is trying to do
when installing or upgrading.

We aim to solve this by not showing some redundant messages, formatting the
packages better, and using color to show specifically what will happen with a
package during install, removal, or an upgrade.


* `Nala Github Repo <https://github.com/volitank/nala>`_
* `Nala: A Beautiful and Structured Frontend for the APT Command <https://trendoceans.com/nala-package-manager/>`_
* `APT sucks, use Nala instead! <https://youtu.be/skbE6U5uE3A>`_


Snap
=======================================

Snaps are app packages for desktop, cloud and IoT that are easy to
install, secure, cross‐platform and dependency‐free.


.. code-block:: console

  $ sudo snap remove obs-studio


**References:**

#. `How to remove a snap package on Ubuntu <https://linuxhint.com/remove-snap-package-ubuntu/>`_
