.. _rhRZX6I3n9:

=======================================
Argparse
=======================================

Optparse is deprecated since 3.2 and all development will continue here.

.. code-block:: python

    # Read a single argument with a value
    parser.add_argument('--id', type=int, nargs=1)

    # Read a single argument with a default
    parser.add_argument('--id', type=int, nargs='?', default=0)

    # Read a flag (boolean) argument
    parser.add_argument('--delete', nargs='?', const=True, default=False)

    # Read multiple arguments
    parser.add_argument('--ids', type=int, nargs='+')

    # Required arguments
    parser.add_argument('--id', type=int, nargs=1, required=True)


References:
=======================================

#. `optparse - Parser for command line options <https://docs.python.org/3/library/optparse.html>`_
#. `Python argparse cheat sheet <https://dev.to/errietta/python-argparse-cheat-sheet-43c3>`_
