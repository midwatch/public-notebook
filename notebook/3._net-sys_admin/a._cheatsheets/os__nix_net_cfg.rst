.. _BamiyZ3Yoc:

=======================================
NIX/Net Config
=======================================

IP
=======================================

.. code-block:: console

    $ ip addr                                                   # Show all ip addr associated on all interfaces
    $ ip -{4|6} addr                                            # Only show IPv4 or IPv6
    $ ip addr show eth0                                         # Only show eth0
    $ ip link ls up                                             # Only show running interfaces

    $ ip addr add {ip_addr/mask} dev {interface}                # Add addr to interface
    $ ip addr add broadcast {ADDDRESS-HERE} dev {interface}

    $ ip addr del {ipv6_addr_OR_ipv4_addr} dev {interface}

    $ ip link set dev {DEVICE} {up|down}                        # Set interface up or down

    $ ip neigh show                                             # Show arp cache

    # Add a new ARP entry
    $ ip neigh add {IP-HERE} lladdr {MAC/LLADDRESS} dev {DEVICE} nud {STATE}

    $ ip neigh del {IPAddress} dev {DEVICE}                     # Delete ARP entry

    $ ip route list
    $ ip route add {NETWORK/MASK} via {GATEWAYIP}
    $ ip route add {NETWORK/MASK} dev {DEVICE}
    $ ip route add default {NETWORK/MASK} dev {DEVICE}
    $ ip route add default {NETWORK/MASK} via {GATEWAYIP}

    $ ip route del default
    $ ip route del 192.168.1.0/24 dev eth0


**Notes:**

* ARP Status Fields:

  * STALE - The neighbour is valid, but is probably already unreachable, so the kernel will try to check it at the first transmission.
  * DELAY – A packet has been sent to the stale neighbour and the kernel is waiting for confirmation.
  * REACHABLE – The neighbour is valid and apparently reachable.

**References:**

#. `Linux IP Command Examples <https://www.cyberciti.biz/faq/linux-ip-command-examples-usage-syntax/>`_
