.. _i8I9N9zUEF:

=======================================
Dataclasses
=======================================

**Data Classes:**

This module provides a decorator and functions for automatically adding
generated special methods such as __init__() and __repr__() to user-defined
classes.

Dataclasses module provides a subset of attrs functionality.

.. code-block:: python

    from dataclasses import dataclass

    @dataclass
    class InventoryItem:
        """Class for keeping track of an item in inventory."""
        name: str
        unit_price: float
        quantity_on_hand: int = 0

        def total_cost(self) -> float:
            return self.unit_price * self.quantity_on_hand

**Attrs:**

attrs is the Python package that will bring back the joy of writing classes by
relieving you from the drudgery of implementing object protocols (aka dunder
methods).


**Pydantic:**

Data validation and settings management using python type annotations. pydantic
enforces type hints at runtime, and provides user friendly errors when data is
invalid.



Tutorials
=======================================

#. `Python dataclasses will save you HOURS, also featuring attrs <https://youtu.be/vBH6GRJ1REM>`_
#. `Do we still need dataclasses? // PYDANTIC tutorial <https://youtu.be/Vj-iU-8_xLs>`_


References
=======================================

#. `dataclasses — Data Classes <https://docs.python.org/3/library/dataclasses.html>`_
#. `attrs: Classes Without Boilerplate <https://www.attrs.org/en/stable/>`_
#. `pydantic-docs <https://pydantic-docs.helpmanual.io/>`_
