.. _p8IJ10ni-u:

=======================================
Syntax Sugar
=======================================


**Tuple Unpacking:**

.. code-block:: python

    x, y, z = 1, 2, 3
    print(f'x: {x} y: {y} z: {z}')
        # x: 1 y: 2 z: 3

    my_tuple = 1, 2
    x, y = my_tuple

    def my_func():
        return (1, 2, 3)

    x, y, z = my_func()
    print(f'x: {x} y: {y} z: {z}')
        # x: 1 y: 2 z: 3

    x, _, z = my_func()
        # Throw away values you don't care about


**Underscores in Numeric Literals:**

.. code-block:: python

    >>> 1_000_000_000_000_000       # Int
        1000000000000000

    >>> 1_000_00.0                  # Float
        100000.0

    >>> 0x_FF_FF_FF_FF              # Hex
        4294967295

    >>> 0b0101_01010101010_0100     # Binary
        174756

    # string formatting
    >>> '{:_}'.format(1000000)
        '1_000_000'

    >>> '{:_x}'.format(0xFFFFFFFF)
        'ffff_ffff'


References
=======================================

#. `Unpacking a Tuple in Python <https://www.geeksforgeeks.org/unpacking-a-tuple-in-python/>`_
#. `PEP 515 – Underscores in Numeric Literals <https://peps.python.org/pep-0515/>`_
