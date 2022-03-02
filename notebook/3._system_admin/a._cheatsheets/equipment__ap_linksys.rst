.. _iEUKJn3b2p:

=======================================
AP - Linksys
=======================================

WRT54GL v 1.1
=======================================

Our favorite get out of jail free WAP/Router.

.. list-table::
    :header-rows: 1

    * - Firmware
      - IP Address
      - Username
      - Password
    * - Linksys
      - 192.168.1.1
      - <none>
      - admin
    * - DD-WRT v2.4
      - 192.168.1.1
      - admin
      - root

The stock Linksys firmware has a limit of 3MB for firmware updates, thus you have to flash the micro or
the mini (below) firware before flashing one of the larger images.

**Resources:**

#. `dd-wrt.v24_mini_generic.bin (r38159) <ftp://ftp.dd-wrt.com/betas/2019/01-02-2019-r38159/broadcom/dd-wrt.v24_mini_generic.bin>`_
#. `Amazon Product Page <https://www.amazon.com/gp/product/B000BTL0OA/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1>`_


Add DHCP Reservation
---------------------------------------

Nagivate to top-level services tab
Click add under DHCP Options block

**Steps:**

#. Navigate to top level `Services` tab
#. Click `add` in DHCP Options block
#. Enter client data (below)
#. Click `Apply Settings`
#. Click `Reboot Router`

.. list-table::
    :header-rows: 1

    * - Option
      - Example Value
    * - MAC Address
      - 88:4a:ea:ca:a3:f9
    * - Hostname
      - My client
    * - IP Address
      - 192.168.1.123
    * - Lease Time
      - 1440 min (1 day), 10080 min (7 days)

**Notes:**

#. The WAP will begin serving the DHCP reservation as soon as `Apply Settings`
   finishes, but we reboot to ensure that the configuration will survive any
   future system restarts.



References
=======================================

#. TBD
