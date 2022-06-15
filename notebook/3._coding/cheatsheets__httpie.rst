.. _luaICuwDdf:

=======================================
HTTPIE
=======================================

An open-source API testing client for open minds.

.. code-block:: console

    $ http :8000/api/platforms/                         # http get localhost port 8000

    $ http POST :8000/api/platforms/ name='buoy 1' desc='buoy 1' serial_number=1

    $ http POST :8000/api/platforms/ < src/tests/_fixtures/data.json


References
=======================================

#. `HTTPIE Docs <https://httpie.org/doc>`_
#. `HTTPIE Cheat Sheet <https://devhints.io/httpie>`_
