.. _cgLgLK2LYJ:

=======================================
SSH
=======================================

General Commands
=======================================

Prevent Adding Host to Known Hosts
---------------------------------------

.. code-block:: console

  $ ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no

  # Set as alias for convience
  $ alias ssh="ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"

  $ ssh <CMD 1>
  $ ssh <CMD 2>
  $ ssh <CMD N>

  $ unalias ssh                                       # Cleanup/remove alias


Run Remote Commands
---------------------------------------

.. code-block:: console

  $ ssh -t USER@HOST '<CMD>'
  $ ssh -t USER@HOST '<CMD 1> && <CMD 2> && <CMD N>'  # Run multiple commands


  -t Force pseudo-terminal allocation.


Key Management
=======================================

Add Keys to Remote Server
---------------------------------------

.. code-block:: console

  $ ssh-copy-id <user>@<host>
  $ ssh-copy-id -i ~/.ssh/<key> <user>@<host>           # Use this key only

Notes:

#. Adding keys enables RSA based authentication.
#. Defaults to using identies listed via ssh-add or ~/.ssh/id_rsa


Add Keys to Agent
---------------------------------------


.. code-block:: console

    $ eval `ssh-agent`
    $ ssh-add ~/.ssh/<key>
    $ ssh-add -l                                        # List loaded keys

Notes:

#. Once keys are loaded into agent no password is required to login to remote
   server.
#. Use keychain to automatically add keys to agent on login.


Add Identity from Remote Server
---------------------------------------

.. code-block:: console

  $ ssh -T git@github.com -o StrictHostKeyChecking=no
  $ sh -c "ssh -T git@github.com -o StrictHostKeyChecking=no; true" [1]

Notes:

#. Convienence function used in Vagrant provision_user.sh script to preload
   Github key on vagrant up. Will not prompt for accept key on first git clone.


Disable Strict Host Key Checking on Local Network
---------------------------------------

Managing continously changing ssh identities, for example reimaging a
beaglebone during testing, can get very anoying. It's trivial to disable
checking on the local network only.

$HOME/.ssh/config

::

    Host 192.168.1.*
        StrictHostKeyChecking no
        UserKnownHostsFile=/dev/null


Notes:

#. SSH does an exact match against the host name. If you define IP above you
   must use the IP of the server for this to work, same if you use a hostname
   (eg: test.example.com)


SSH Forwarding
=======================================


Credentials and Env Variables
---------------------------------------

.. code-block:: console

    # Enable agent forwarding [1]
    $ ssh -A

    $ ssh foo@host "FOO=foo BAR=bar doz"
    $ cat secret_info | ssh foo@host remote_program

Notes:

#. Allows us to use our ssh-agent keys on remote machine without installing the
   keys on that machine.
#. Envars requires changing server and client config (AcceptEnv and SendEnv)


Ports
---------------------------------------

.. code-block:: console

    $ ssh -A                                            # Enable agent forwarding [1]

    $ ssh -X nosuchuser@nospam.org                      # Enable X11 forwarding

    $ ssh -L 80:intra.exmaple.com:80 gw.example.com     # Local port forwarding [2]

    $ ssh -R 8080:localhost:80 public.example.com       # Remote port forwarding [3]

Notes:

#. Open connection for gw.example.com and forward any connection to port 80
   on intra.example.com.
#. Allow anyone on remote server to connect to TCP port 8080 on remote server.
   This will be tunneled back to client host on port 80.


Install SSH Server
=======================================

.. code-block:: console

    $ sudo apt install -y openssh-server

Notes:

#. SSH Server is not installed by default on Ubuntu Xenial (16.04)


References
=======================================

#. `SSH Port Forwarding Example <https://www.ssh.com/ssh/tunneling/example>`_
#. `SSH Key Management <https://serverfault.com/a/115336>`_
#. `Tip #3 Keychain <https://help.ubuntu.com/community/QuickTips>`_
#. `Forward Env Var over SSH <https://stackoverflow.com/a/4410137>`_
#. `Run / Execute Command Using SSH <https://www.cyberciti.biz/faq/unix-linux-execute-command-using-ssh/>`_
#. `How To Run Multiple SSH Command On Remote Machine And Exit Safely <https://www.cyberciti.biz/faq/linux-unix-osx-bsd-ssh-run-command-on-remote-machine-server/>`_
