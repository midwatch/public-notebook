.. _hIpBuraeYe:

=======================================
PIP/PIPX
=======================================

PIP
===============================================================================

.. code-block:: console

    $ sudo python3 -m pip install <package>
    $ sudo python3 -m pip install --upgrade <package>
    $ sudo python3 -m pip install -e path/to/some/package       - install in 'editable mode'
    $ sudo python3 -m pip install -e \
        git+http://repo/my_project.git#egg=some_project

    $ sudo python3 -m pip install \                             - Use in addition to index-url
        --extra-url <url> \
        package

    $ sudo python3 -m pip install \                             - install package from alternate index
        --index-url <url> \
        <package>

    $ python3 -m pip index versions <package>                   - list available versions of package

    $ echo $PIP_INDEX_URL="<url>"
    $ sudo -E python3 -m pip install <package>                  - install package from alternate index

    # Install all of your application’s dependencies into the myapp directory
    # Usefull for Zipapp
    $ python -m pip install -r requirements.txt --target myapp

    other options:
    --find-links    If url or path to an html file, then parse for links to archives.
                    If a local path or file:// url then look for archives in directory
                    listing.

    --user          Install packages into your user Python environment

    install from test.pypi.org:

    $ python3 -m pip install --index-url https://test.pypi.org/simple/ <package>


**Notes:**

a. Use python3 -m pip to prevent breaking of distrbution pip/pip3 wrapper
b. `devpi use <url>` command will set the global index-url for pip and
   it will install packages from there.

**References:**

#. `pip install <https://pip.pypa.io/en/stable/reference/pip_install/>`_


PIPX
===============================================================================

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

**References:**

#. `Github <https://github.com/pypa/pipx>`_
#. `Docs <https://pypa.github.io/pipx/>`_
#. `Comparison to Other Tools <https://pypa.github.io/pipx/comparisons/>`_

