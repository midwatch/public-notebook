.. _mrXC1nmrc8:

=======================================
Basic Syntax
=======================================

`Built-in Functions <https://docs.python.org/3/library/functions.html>`_

`Built-in Types <https://docs.python.org/3/library/stdtypes.html>`_

* Truth value testing
* Boolean operations
* Comparisons (<, <=, ==, etc)
* Numeric operations (+, -, *, etc)
* Bitwise operations


Exceptions
=======================================

`Built-in Exceptions <https://docs.python.org/3/library/exceptions.html>`_

.. code-block:: python

    try:
        do_something()

    except ValueError:
        handle_err()

    except ValueError as err
        handle_err()
        logging.exception(err)

    except (RuntimeError, TypeError, NameError):
        handle_err()

    except Exception as err:
        print(type(err))    # the exception instance
        print(err.args)     # arguments stored in .args
        print(err)          # __str__ allows args to be printed directly

    else:
        # Code that is executed if the try clause does not raise an exception
        pass

    finally:
        # The finally clause runs whether or not the try statement produces
        # an exception
        pass


**Anti-Patterns:**

.. code-block:: python

    # Blindly consume exceptions
    try:
        do_something()

    except Exception:
        # masks every exception upto and including syntax errors
        pass


    # Bare except swallows everything including CTRL-C
    try:
        do_something()

    except:
        pass



Flow Control
=======================================

If/Then
---------------------------------------

.. code-block:: python

    if x < 0:
        pass

    elif x == 0:
        pass

    else:
        pass

**Anti-Patterns:**

.. code-block:: python

    # Nested if statements, use guard clauses instead.

    def my_function(wifi, login, admin):
        if not wifi:
            log.debug('Must be connected to WiFi')
            return

        if not login:
            log.debug('Must login to your account')
            return

        if not admin:
            log.debug('Must be an admin')
            return

        do_something()


Looping Speed
---------------------------------------

The fastest way to loop in Python is to not loop in Python.

#. Mathmatically compute the answer ahead of time if possible
#. Have the work done in a pure c function (numpy)
#. Use Python builtins like sum() or map()
#. For loop/comprehension
#. While loop


For Loop
---------------------------------------

.. code-block:: python

    for word in ['cat', 'window', 'defenestrate']:
        print(word)

    for num in range(5):
        print(num)

    for x in [1, 2, 3]:
        if x == y:
            print(f'{x} == {y}')
            break

        else:
            # loop fell through
            print(f'{y} not found in sequence')

    for num in range(2, 10):
        if num % 2 == 0:
            print(f'Found an even number {num}`)
            continue

        print(f'Found an odd number {num}')

    for idx, val in enumerate(range(5)):
        print(f'{idx}: val)

    a = [1,2,3]
    b = [4,5,6]
    for av, bv in zip(a,b):
        print(f'{av} - {bv}')
        # 1 - 4
        # ...
        # 3 - 6

    a = [1,2,3]
    b = [4,5,6]
    for idx, (av, bv) in enumerate(zip(a,b)):
        print(f'{idx} - {av} - {bv}')
        # 0 - 1 - 4

    for key in dict:
        pass

    for key, val in dict.items()
        pass


Comprehensions
---------------------------------------

Construct new sequences (lists, set, dics, etc) from an existing sequence.

* Rewrite loops and map() calls
* Replace filter() via conditional logic

.. code-block:: python

    # General patterns

    new_seq = [expression for member in iterable]
    new_seq = [expression for member in iterable (if conditional)]

    dict_comp = {i: i*i for i in range(10)}
    list_comp = [x*x for x in range(10)]
    set_comp = {i%3 for i in range(10)}         # {} overlaps with dict
    gen_comp = (2*x+5 for x in range(10))


Dictionary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    state = ['Gujarat', 'Maharashtra', 'Rajasthan']
    capital = ['Gandhinagar', 'Mumbai', 'Jaipur']

    dict_using_comp = {key:value for (key, value) in zip(state, capital)}



Generator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generators generate each value one by one, making them more memory efficient.

.. code-block:: python

    input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
    output_gen = (var for var in input_list if var % 2 == 0)

    for var in output_gen:
        do_something(var)



List
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    new_list = [var**2 for var in range(1, 10)]



Set
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

    new_set = {var for var in input_list}


While Loop
---------------------------------------

.. code-block:: python

    while True:
        do_something()

    with open('example.txt', 'rb') as fd_in:
        while (chunk := f.read(4)) != b'':          # walrus operator
            print(f'chunk: {chunk}')


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

#. `More Control Flow Tools <https://docs.python.org/3/tutorial/controlflow.html>`_
#. `Python's secret second argument to iter() <https://youtu.be/YC-12-0sXR8>`_
#. `The Walrus Operator: Python 3.8 Assignment Expressions <https://realpython.com/python-walrus-operator/>`_
#. `Comprehensions in Python <https://www.geeksforgeeks.org/comprehensions-in-python/>`_
#. `When to Use a List Comprehension in Python <When to Use a List Comprehension in Python>`_
#. `25 nooby Python habits you need to ditch <https://youtu.be/qUeud6DvOWI>`_
#. `Exceptional logging of exceptions in Python <https://www.loggly.com/blog/exceptional-logging-of-exceptions-in-python/>`_
#. `Python Operators <https://mindmajix.com/python/basic-operators-in-python>`_
#. `The Fastest Way to Loop in Python - An Unfortunate Truth <https://youtu.be/Qgevy75co8c>`_
#. `Nesting "If Statements" Is Bad. Do This Instead. <https://youtu.be/ZzwWWut_ibU>`_
#. `Positional-only and keyword-only arguments in Python <https://youtu.be/R8-oAqCgHag>`_
