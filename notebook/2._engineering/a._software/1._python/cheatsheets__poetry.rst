.. _ZQIQyA6KTc:

=======================================
Poetry
=======================================

Python packaging and dependency management made easy.

.. code-block:: console

    # Install solution and dependencies
    $ poetry install

    # Install dependencies only
    $ poetry install --no-root

    # Add depencency
    $ poetry add pendulum

    # Update dependencies to latest versions
    $ poetry update

    # Run cmd in poetry virtual environment
    $ poetry run python your_script.py
    $ poetry run pytest


Notes:
=======================================

Poetry will try to find a common version of a dependency across all specified
Python versions.

    EX: we put python="*" in pyproject.py and it installed a very old version,
    presumably 2.7 compliant, of a depencency that wouldn't work with our installed
    environment.


References:
=======================================

#. `Poetry - Docs <https://python-poetry.org/docs/>`_
#. `Poetry - pyproject.toml <https://python-poetry.org/docs/pyproject/>`_
#. `Clarifying PEP 518 (a.k.a. pyproject.toml) <https://snarky.ca/clarifying-pep-518/>`_
#. `What the heck is pyproject.toml? <https://snarky.ca/what-the-heck-is-pyproject-toml/>`_
