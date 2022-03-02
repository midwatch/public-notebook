.. _o5WgXatB3n:

=======================================
API Doc Strings
=======================================

Sphinx API Doc
=======================================

.. code-block:: python

    """[Summary]

    :param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
    :type [ParamName]: [ParamType](, optional)
    ...
    :raises [ErrorType]: [ErrorDescription]
    ...
    :return: [ReturnDescription]
    :rtype: [ReturnType]
    """

    class SimpleBleDevice(Peripheral):
        """This is a conceptual class representation of a simple BLE device (GATT Server). It is
        essentially an extended combination of the :class:`bluepy.btle.Peripheral`
        and :class:`bluepy.btle.ScanEntry` classes

        :param client: A handle to the :class:`simpleble.SimpleBleClient` client object that
                       detected the device
        :type client: class:`simpleble.SimpleBleClient`
        :param addr: Device MAC address, defaults to None
        :type addr: str, optional
        :param addrType: Device address type - one of ADDR_TYPE_PUBLIC or ADDR_TYPE_RANDOM,
                         defaults to ADDR_TYPE_PUBLIC
        :type addrType: str, optional
        :param iface: Bluetooth interface number (0 = /dev/hci0) used for the connection,
                      defaults to 0
        :type iface: int, optional
        :param data: A list of tuples (adtype, description, value) containing the AD type code,
                     human-readable description and value for all available advertising data items,
                     defaults to None
        :type data: list, optional
        :param rssi: Received Signal Strength Indication for the last received broadcast from the
                     device. This is an integer value measured in dB, where 0 dB is the maximum
                     (theoretical) signal strength, and more negative numbers indicate a weaker
                     signal, defaults to 0
        :type rssi: int, optional
        :param connectable: `True` if the device supports connections, and `False` otherwise
                            (typically used for advertising ‘beacons’)., defaults to `False`
        :type connectable: bool, optional
        :param updateCount: Integer count of the number of advertising packets received from the
                            device so far, defaults to 0
        :type updateCount: int, optional
        """

    def getServices(self, uuids=None):
        """Returns a list of :class:`bluepy.blte.Service` objects representing the services
        offered by the device. This will perform Bluetooth service discovery if this has not
        already been done; otherwise it will return a cached list of services immediately..

        :param uuids: A list of string service UUIDs to be discovered, defaults to None
        :type uuids: list, optional
        :return: A list of the discovered :class:`bluepy.blte.Service` objects, which match the
        provided ``uuids``
        :rtype: list On Python 3.x, this returns a dictionary view object, not a list
        """




References
=======================================

#.  `PEP 8 - Style Guide for Python Code <http://www.python.org/dev/peps/pep-0008/>`_
#.  `PEP 257 - Docstring Conventions <https://www.python.org/dev/peps/pep-0257/>`_
#.  `Sphinx reStrcturedText Primer <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
#.  `pydocstyle <https://github.com/PyCQA/pydocstyle>`_
#.  `Sphinx <https://pypi.org/project/Sphinx/>`_
