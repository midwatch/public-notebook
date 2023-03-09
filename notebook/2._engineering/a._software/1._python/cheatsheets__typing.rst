.. _KwRA0gGIFj:

=======================================
Typing
=======================================

Python’s type hints provide you with optional static typing to leverage the best
of both static and dynamic typing.

.. code-block:: python

    name: str = "bob"
    name = 100          # error detected

    def my_function(name: str) -> None:
        print(f'hello {name}')

    my_function(name)
    my_function(1)      # error detected


    #Set type hints for multiple types
    from typing import Union
    def add (x: Union(int, float), y: Union[int, float]) -> Union[int, float]:
        return x + y

    # use an alias
    number = Union[int, float]
    def add(x: number, y: number) -> number:
        return x + y

Type aliases from typing module:

.. list-table::
   :header-rows: 1

   * - Alias
     - Built-in Type
     - Alias
     - Built-in Type
   * - List
     - list
     - Frozenset
     - frozenset
   * - Dict
     - dict
     - Sequence
     - For list, tuple, and any other sequence type
   * - Set
     - set
     - Mapping
     - For dict, set, frozenset, and any other mapping data type
   * - Tuple
     - tuple
     - ByteString
     - bytes, bytearray, and memoryview types.

.. code-block:: python

    from typing import List

    ratings: List[int] = [1, 2, 3]


Mypy
=======================================

A static type checker for Python and is designed with gradual typing in mind.

.. code-block:: console

    $ mypy program.py
    $ mypy <python pkg>
    $ mypy --disallow-untyped-defs <python pkg>
    $ mypy --strict <python pkg>

Mypy requires type annotations for every imported module to pass without errors
and stub files for commonly used modules are available from the
`typeshed project <https://github.com/python/typeshed/tree/master/stubs>`_

.. code-block:: console

    $ python3 -m pip install types-requests


IDE Integrations
---------------------------------------

*   `Sublime Text <https://github.com/fredcallaway/SublimeLinter-contrib-mypy>`_


References
=======================================

#. `typing module <https://docs.python.org/3/library/typing.html>`_
#. `Python Type Hints <https://www.pythontutorial.net/python-basics/python-type-hints/>`_
#. `Mypy Github <https://github.com/python/mypy>`_
#. `Mypy docs <https://mypy.readthedocs.io/en/stable/>`_
#. `Mypy cheat sheet <https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html>`_
#. `Mypy w/ existing code <https://mypy.readthedocs.io/en/stable/existing_code.html>`_
#. `Automatic stub generation <https://mypy.readthedocs.io/en/stable/stubgen.html>`_
