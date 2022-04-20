.. _p8IJ10ni-u:

=======================================
Syntax Sugar
=======================================


**Underscores in Numeric Literals:**

PEP 515 adds the ability to use underscores in numeric literals for improved
readability.

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

#. `PEP 515 – Underscores in Numeric Literals <https://peps.python.org/pep-0515/>`_
