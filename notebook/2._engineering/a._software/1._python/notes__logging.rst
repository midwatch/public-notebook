.. _EJUdcc17ls:

=======================================
Logging
=======================================

Use print() for ordinary console output.

Logging output defaults to sys.stderr

`When to use logging <https://docs.python.org/3.8/howto/logging.html#when-to-use-logging>`_

**Log Message Formatting:**

The logging module was added when only the printf string formatting was
available and it can't be changed without breaking backwards compatibility.
Thus, all strings must/should us printf format.

`printf-style String Formatting <https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting>`_

.. code-block:: python

    logging.warning('%s before you %s', 'Look', 'leap!')


BasicConfig
=======================================

`BasicConfig Options <https://docs.python.org/3.8/library/logging.html#logging.basicConfig>`_

Default Format: severity:logger name:message

.. code-block:: python

    # mylib/__init__.py
    import logging
    log = logging.getLogger(__name__)

    def do_something():
        log.info('doing something')

    # mylib/mymodule.py
    import logging
    log = logging.getLogger(__name__)

    def do_something():
        log.info('doing something')

    def raise_err():

        1/0

    # my_program.py
    import logging
    import mylib
    from mylib import mymodule

    logging.basicConfig(level=logging.DEBUG)    # default level = Warning
    log = logging.getLogger(__name__)
    log.debug('This message should appear on the console')

    mylib.do_something()
    mymodule.do_something()
    mymodule.raise_err()



    # Console Output:
    # ############################

    # $ python3 log_test.py 2> /dev/null
    #     normal console output

    # $ python3 log_test.py
    #     normal console output

    #     DEBUG:__main__:This message should appear on the console
    #     INFO:mylib:doing something
    #     INFO:mylib.mymodule:doing something
    #     ERROR:mylib.mymodule:division by zero
    #     Traceback (most recent call last):
    #       File "/home/justin/tmp/mylib/mymodule.py", line 12, in raise_err
    #         1/0
    #     ZeroDivisionError: division by zero


Examples
---------------------------------------

.. code-block:: python

    logging.basicConfig(filename='example.log',level=logging.DEBUG)
    logging.basicConfig(format='%(levelname)s:%(message)s')
        # WARNING:And this, too

    logging.basicConfig(format='%(asctime)s %(message)s')
        # 2010-12-12 11:41:42,612 is when this event was logged.

    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # 12/12/2010 11:46:36 AM is when this event was logged.


References
=======================================

#. `Logging facility for Python <https://docs.python.org/3.8/library/logging.html>`_
#. `Basic Logging Tutorial <https://docs.python.org/3.8/howto/logging.html#logging-basic-tutorial>`_
