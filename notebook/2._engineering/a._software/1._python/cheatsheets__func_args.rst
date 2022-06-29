.. _ZxokzBcUDw:

=======================================
Function Arguments
=======================================

.. code-block:: python

    # unspecified argument requirements
    def f(a, b, c, *args, **kwargs):
        # can pass as either positional or keyword
        # f(1, 2, 3)
        # f(a=1, b=2, c=3)  order doesn't matter
        # f(1, c=3, b=2)    mix and match (positional args must come first)


    # specify positional, keyword, or both
    def f(pos_only, /, pos_or_kw, *, kw_only)


    # pos_only
    def f(x, y, /):
        # good for functions where the arguments don't have anykind of
        # intrinsic meaning (eg x * y)


    # kw_only
    def g(a, b, *, kw_only):
        # forcing keywords helps enforce correct usage by requiring the caller
        # to spell out exactly what they're passing in so they don't mix
        # up args (eg price & quantity)
        # Will raise an error on extra positional args


    # pos_only and kw_only
    def f(a, /, *, c):

        def dataclass(cls=None, /, *, init=True, repr=True, ...):

        def f(x, y, /, *, mod):
            return (x ** y) % mod

        x = f(3, 50, mod=17)


    # all three (pos_only, pos_or_kw, & kw_only)
    def f(a, /, b, *, c):
        pass

        # There are zero examples of this in the std library (not counting
        # the unit tests...)






**Notes:**

#. *args eats all remaining positional arguments
#. **kwargs catches all remaining keyword arguments


References
=======================================

#. `Positional-only and keyword-only arguments in Python <https://youtu.be/R8-oAqCgHag>`_

