.. _rJaf0ZL95k:

=======================================
Comparisons
=======================================

Every object has an identity, a type and a value.

.. code-block:: text

    identity:   an integer id that is garunteed to be unique and constant
                throughout its lifetime.

                is compares two objects for identity.

    type:       isinstance(object, classinfo) built-in function is recommended
                for testing the type of an object, because it takes subclasses
                into account.

                issubclass(class, classinfo) returns True is class is a subclass
                (dirent, indirect, or virtual) of given class.

    value:      == compares two objects for equality


Tests
=======================================

Membership
---------------------------------------

.. code-block:: python

    if 1 in [1, 2, 3]:
        pass

    if 4 not in [1, 2, 3]:
        pass

    if 1 in {1: 'one', 2: 'two', 3: 'three'}:
        pass

    if 'bob' in 'hello bob':
        pass


Truth
---------------------------------------

.. code-block:: python

    true_value = "aaa"  # truthy
    false_value = []    # falsey
    none_value = None

    if true_value:
        pass

    if not false_value:
        pass

    if none_value is None:
        pass


Type
---------------------------------------

.. code-block:: python

    numbers = [1, 2, 3, 4, 2, 5]

    if isinstance(numbers, list):
        pass


References
=======================================

#. `Data model <https://docs.python.org/3/reference/datamodel.html>`_
#. `Comparison in Python is Not as Simple as You May Think <https://towardsdatascience.com/comparison-in-python-is-not-as-simple-as-you-may-think-a83eec69ab54>`_

#. `Truth Value Testing <https://realpython.com/lessons/truth-value-testing/>`_
