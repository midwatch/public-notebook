.. _HWm5hMe0E7:

=======================================
String Formatting
=======================================

Using Quotes:

* Double Quotes ("): strings that are used for interpolation and/or are that intended for the end-user to see
* Single Quotes ('): everything else


F-Strings
=======================================

PEP 498 - Literal String Interpolation; new in 3.6.

.. warning:: If your format strings are user-supplied, use Template Strings to avoid security issues.


.. code-block:: python

    name = "Eric"
    age = 74
    f"Hello, {name}, You are {age}"
    # 'Hello, Eric. You are 74.'

    # Arbitrary Expressions
    f"{2 * 37}
    # '74'

    # Call functions
    def to_lowercase(input):
        return input.lower()

    name = "Eric Idle"
    f"{to_lowercase(name)} is funny."
    # 'eric idle is funny.'

    f"{name.lower()} is funny."
    'eric idle is funny.'

    # Multiline f-Strings
    message = f"Hi {name}. " \
              f"You are a {profession}. " \
              f"You were in {affiliation}."

    # 'Hi Eric. You are a comedian. You were in Monty Python.'

**Format Specifiers:**

.. code-block:: python

    # Rounding
    print(f'The value of pi is approximately {math.pi:.3f}.')
    # The value of pi is approximately 3.142.

    # Padding
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    for name, phone in table.items():
        print(f'{name:10} ==> {phone:10d}')

    # Sjoerd     ==>       4127
    # Jack       ==>       4098
    # Dcab       ==>       7678

Other modifiers can be used to convert the value before it is formatted:

* '!a' applies ascii()
* '!s' applies str()
* '!r' applies repr()


Template Strings
=======================================

.. note:: Template strings don’t allow format specifiers, so you'll have to manually tranform formats

.. code-block:: python

    from string import Template
    t = Template('Hey, $name!')
    t.substitute(name=name)
    # 'Hey, Bob!'

    # Manual transform
    templ_string = 'Hey $name, there is a $error error!'
    Template(templ_string).substitute(name=name, error=hex(errno))
    # 'Hey Bob, there is a 0xbadc0ffee error!'


    # Safe Substitute
    # Uses original placeholder instead of rasing KeyError on missing arg(s)
    from string import Template
    s = Template('$who likes $what')
    d = dict(who='tim')
    Template('$who likes $what').safe_substitute(d)
    # 'tim likes $what'


References:
=======================================

#. https://www.python.org/dev/peps/pep-0498/
#. https://docs.python.org/3/reference/lexical_analysis.html#f-strings
#. https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings
#. https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python
#. https://realpython.com/python-string-formatting/
#. https://docs.python.org/3/library/string.html#formatspec
