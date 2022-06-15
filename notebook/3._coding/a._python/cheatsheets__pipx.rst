.. _nZUfFVgXG2:

=======================================
pipx
=======================================

Install and Run Python Applications in Isolated Environments.

Installs Python apps in $USER/.local/bin without requiring sudo and independant
of the system wide package dirs.


.. code-block:: shell

    # Install pipx
    $ sudo apt-get install -y python3-venv      # Ubuntu dependency
    $ python3 -m pip install --user pipx
    $ python3 -m pipx ensurepath

    # restart terminal

    $ pipx --version
        0.16.4


    # Usage
    $ pipx install <package>
    $ pipx list                                 # List installed

    $ pipx upgrade <package>
    $ pipx upgrade-all

    $ pipx uninstall <package>


    # Run in temporary virtual environment
    $ pipx run APP [ARGS...]


References:
=======================================

#. `Github <https://github.com/pypa/pipx>`_
#. `Docs <https://pypa.github.io/pipx/>`_
#. `Comparison to Other Tools <https://pypa.github.io/pipx/comparisons/>`_
