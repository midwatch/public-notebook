.. _Q812f9cb6b:

=======================================
Packaging
=======================================

Zipapp
=======================================

Using the zipapp module, it is possible to create self-contained Python
programs, which can be distributed to end users who only need to have a suitable
version of Python installed on their system.

The steps to create a standalone archive are as follows:

#. Create your application in a directory as normal, so you have a myapp directory
   containing a __main__.py file, and any supporting application code.

#.  Install all of your application’s dependencies into the myapp directory, using pip:

    $ python -m pip install -r requirements.txt --target myapp

    this assumes you have your project requirements in a requirements.txt file - if
    not, you can just list the dependencies manually on the pip command line

#.  Optionally, delete the .dist-info directories created by pip in the myapp directory.
    These hold metadata for pip to manage the packages, and as you won’t be making any
    further use of pip they aren’t required - although it won’t do any harm if you leave
    them.

3.  Package the application using:

    $ python -m zipapp -p "interpreter" myapp

This will produce a standalone executable, which can be run on any machine with
the appropriate interpreter available.

**Cavets:**

#. If your application depends on a package that includes a C extension, that package
   cannot be run from a zip file
#. If you are shipping a Windows executable you either need to ensure that your users
   have python3.dll on their PATH (which is not the default behaviour of the installer)
#. In your application, sys.executable will be your application. If your application
   uses the multiprocessing module, it will need to call multiprocessing.set_executable()
   to let the module know where to find the standard Python interpreter.


**Example:**

.. code-block:: console

    $ python -m zipapp source [options]

    $ python -m zipapp myapp -m "myapp:main"
    $ python myapp.pyz
        # <output from myapp>

    # To make the application directly executable on POSIX,
    # specify an interpreter to use.
    $ python -m zipapp myapp -p "/usr/bin/env python"
    $ ./myapp.pyz
        # <output from myapp>


PyInstaller
=======================================

PyInstaller gives you the ability to create a folder or executable that users
can immediately run without any extra installation. Your users won’t even know
they’re running a Python project because the Python Interpreter itself is
bundled into your application.

Main Capabilities:

* Package for Windows, OSX, and Linux
* Python3
* Single file

Steps Required:

#. Create an entry point script outside of the package to run it.
#. Identify any hidden imports
#. Package using PyInstaller

**Example:**

.. code-block:: python

    # Example entrypoint script cli.py
    from reader.__main__ import main

    if __name__ == '__main__':
        main()


.. code-block:: console

   $ pyinstaller src/clip-article/cli.py \
                 --add-data "/usr/local/lib/python3.8/dist-packages/goose3:goose3" \
                 --add-data "/usr/local/lib/python3.8/dist-packages/newspaper:newspaper" \
                 --distpath dist/ \
                 --workpath build/clip-article \
                 --paths /usr/local/lib/python3.6/dist-packages \
                 --name clip-article \
                 --onefile


**Notes:**

#. --add-data Copy module data files into the generated binary
#. --paths Tell pyinstaller where to look for installed modules
#. --name The name of the generated binary


Pip Tools
=======================================

A set of command line tools to help you keep your pip-based packages fresh, even
when you've pinned them. You do pin them, right?

* `GitHub <https://github.com/jazzband/pip-tools>`_


References
=======================================

#. `Zipapp - Manage executable Python zip archives <https://docs.python.org/3/library/zipapp.html>`_
#. `Freezing Your Code <https://docs.python-guide.org/shipping/freezing/>`_
#. `PyInstaller Manual <https://pyinstaller.readthedocs.io/en/stable/>`_
#. `Using PyInstaller to Easily Distribute Python Applications <https://realpython.com/pyinstaller-python/>`_
