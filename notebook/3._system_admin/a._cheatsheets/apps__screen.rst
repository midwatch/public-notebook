.. _t5-frmG5t4:

=======================================
Screen
=======================================

Show all commands
=======================================

.. code-block:: console

    $ Ctrl-A ?

Detach screen
=======================================

.. code-block:: console

    $ Ctrl-A d

Re-attach screen
=======================================

.. code-block:: console

    $ screen -r

    $ screen -ls                # List all screen sessions

    $ screen -r <session id>

Logging actions
=======================================

.. code-block:: console

    $ Ctrl-A H                  # Will log to file in ~/

    or

    $ screen -L

Lock screen
=======================================

.. code-block:: console

    $ Ctrl-A x

Leave Screen
=======================================

.. code-block:: console

    $ Ctrl-A d                  # Detach
    $ Ctrl-A K                  # Kill

References
=======================================

#. `10 Screen Command Examples <https://www.tecmint.com/screen-command-examples-to-manage-linux-terminals/>`_.
