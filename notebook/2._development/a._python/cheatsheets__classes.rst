.. _uhkbT3EtJv:

=======================================
Classes
=======================================

.. code-block:: python

    class MyClass:
    class MyClass(ParentClass):

        __slots__ == 'x', 'y', 'z'
        # Saves on memory usage when you have a lot of really small objects
        # removes __dict__ atrribute
        # can't add new attributes at run time

        @staticmethod
        def static_method(x):
            # A method that does not rely on a specific instance of a class and are
            # pretty uncommon in practice

            # MyClass.static_method(x)


        @classmethod
        def class_method(cls, x)
            # Typically used for alternate constructors (eg MyClass.from_json(fd))

            # new_instance = cls()
            # ...
            # return new_instance


        def __new__(cls, *args, **kwargs):
            # Responsible for creating and returning the actual object.
            # Intercept and modify the arguments before the object is created

            # Overlaps with factory pattern

            # ...
            # return super().__new__(cls)


        def __init__(self, *args, **kwargs):
            # Responsonsible for initializing the object, setting default values, etc.

            super().__init__()              # Call parent's __init__ method,
                                            # optional

        def __format__(self, format_spec):
            # evaluation of formatted string literals and the str.format() method,
            # to produce a “formatted” string representation of an object
            # (eg float precision, datetime, etc)


        def __repr__(self):
            # compute the “official” string representation of an object.
            # If at all possible, this should look like a valid Python
            # expression that could be used to recreate an object with the same
            # value


        def __str__(self):
            # compute the “informal” or nicely printable string representation of
            # an object


        @property
        def my_var(self):
            return self._my_var


        @my_var.setter
        def my_var(self, value)
            self._my_var = value

        @my_var.deleter
        def my_var(self):
            del self._my_var

        def instance_method(self, x):
            # Bog standard class method

            super().instance_method(x)       # call parent's instance_method

**Notes:**

#. Use @dataclass to automatically create the standard dunder methods

References
=======================================

#. `Python __slots__ and object layout explained <https://youtu.be/Iwf17zsDAnY>`_
#. `Python staticmethod and classmethod <https://youtu.be/SXApHXsDe8I>`_
#. `__new__ vs __init__ in Python <https://youtu.be/-zsV0_QrfTw>`_
#. `super, Python's most misunderstood feature <https://youtu.be/X1PQ7zzltz4>`_
#. `Data model <https://docs.python.org/3/reference/datamodel.html#object.__repr__>`_
#. `Property decorator <https://docs.python.org/3/library/functions.html#property>`_
#. `dataclassses <https://docs.python.org/3/library/dataclasses.html>`_
#. `A Guide to Python's Magic Methods <https://rszalski.github.io/magicmethods/>`_
