.. _8ABZ9UKu62:

=======================================
Mac OSX
=======================================

General
=======================================

Printers
---------------------------------------

.. code-block:: console

    $ lp filename
    $ lpr -P printername filename.pdf
    $ lpstat                                # show printer names


**Notes:**

#. Supported file types: Plain text, PDF, & PostScript


Management
=======================================

Mac Ports
---------------------------------------

**Routine Usage:**

.. code-block:: console

    $ sudo port -d selfupdate
    $ sudo port upgrade outdated

    $ port search --name --glob 'php*'
    $ port search --name --line --glob 'php*'
    $ port search --name --line --regex '^php\d*$'

    $ port search rrd

    $ sudo port select --set python python36
    $ sudo port select --set python3 python36

    $ sudo port install python36
    $ sudo port select --set python3 python36

    $ sudo port install py36-pip
    $ sudo python3 -m pip install --upgrade pip


**Migration:**

Install OS X version specific Mac ports release; see Mac Ports Migration (below)

.. code-block:: console

    # Backup current configuration
    $ port -qv installed > myports.txt
    $ port echo requested | cut -d ' ' -f 1 | uniq > requested.txt
    $ sudo port -f uninstall installed
    $ sudo rm -rf /opt/local/var/macports/build/*

    # Migrate confguration to new version
    $ curl --location --remote-name https://github.com/macports/macports-contrib/raw/master/restore_ports/restore_ports.tcl
    $ chmod +x restore_ports.tcl
    $ xattr -d com.apple.quarantine restore_ports.tcl
    $ sudo ./restore_ports.tcl myports.txt

    # Rebuild selected ports
    $ sudo port unsetrequested installed
    $ xargs sudo port setrequested < requested.txt


**Notes:**

#. Mac ports builds are tied to the major Darwin release and will require migration when the base
   OS is upgraded.
#. xattr -d com.apple.quarantine restore_ports.tcl will return an error if the quarintine property
   isn't set, disregard.
#. Mac ports builds all software locally (BSD style) and thus upgrade
   outdated can take a significant amount of time.



References
=======================================

#. `Mac Ports Guide <https://guide.macports.org/>`_
#. `Printing from the Command Line <https://www.oreilly.com/library/view/running-mac-os/0596009135/ch10s06.html>`_
#. `Possible to print to PDF from Mac terminal? <https://superuser.com/a/607380>`_
#. `Mac Ports Migration <https://trac.macports.org/wiki/Migration>`_
#. `Restore Ports Script <https://raw.githubusercontent.com/macports/macports-contrib/master/restore_ports/restore_ports.tcl>`_
