.. _uEJCtlATid:

=======================================
SBC/Raspberry PI
=======================================

Hardware
=======================================

.. figure:: _include/images/rpi_3_header.png
    :scale: 50 %


Power
---------------------------------------

RPI3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2.4A Max (typical: 400 - 1300mA)

.. list-table::
    :header-rows: 1

    * - Function
      - Imax (mA)
    * - Camera
      - 250
    * - Ethernet
      - ?
    * - GPIO Pins
      - 100
    * - HDMI
      - 50
    * - Wifi
      - ?

I/O Pins
---------------------------------------

GPIO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**sysfs:**

.. code-block:: console

  $ echo <pin number> > /sys/class/gpio/export

  # For GPIO 4
  $ echo 4 > /sys/class/gpio/export

  $ ls /sys/class/gpio/gpio4:

    * active_low
    * direction
    * edge
    * uevent
    * value

  $ cat /sys/class/gpio/gpio<pin number>/value

  $ echo out > /sys/class/gpio/gpio<pin number>/direction

  $ echo 0 > /sys/class/gpio/gpio<pin number>/value

  $ echo 1 > /sys/class/gpio/gpio<pin number>/value

I2C
---------------------------------------

Serial
---------------------------------------

**Debug Console:**


Using Adafruit USB to TTL Serial Cable.

**Enable Console:**

    add enable_uart=1 to bottom of /boot/config.txt

    or

    use raspi-config

**Connect Leads:**

.. list-table::
    :header-rows: 1

    * - Cable Wire Color
      - RPI Header Pin
      - Pin Function
    * - Black
      - 6
      - GND
    * - White
      - 8
      - TXD
    * - Green
      - 10
      - RXD

SPI
---------------------------------------

Operating Systems
=======================================

Alpine Linux
---------------------------------------

Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Steps:**

#. Create SD Card
#. First Boot


**Create SD Card:**

.. code-block:: console

    $ sudo -i

    $ dmesg | tail
        > sdh: sdh1 sdh2

    $ SD_DISK="sdh"
    $ VERSION="v3.8"
    $ ARCH="aarch64"
    $ URL="http://dl-cdn.alpinelinux.org/alpine/$VERSION/releases/$ARCH/alpine-rpi-3.8.0-$ARCH.tar.gz"

    $ fdisk /dev/$SD_DISK
        > d - delete partitions
        > n - create new partition
        > t - set partition type (c)
        > a - set bootable flag
        > p

        Device     Boot Start      End  Sectors  Size Id Type
        /dev/sdh1  *     2048 31116287 31114240 14.9G  c W95 FAT32 (LBA)

        > w - write and exit

    $ mkfs.fat -F 32 /dev/${SD_DISK}1
    $ mount /dev/${SD_DISK}1 /mnt/usb
    $ cd /mnt/usb

    $ curl $URL | tar xvzf - --no-same-owner

    $ sed -i -e 's/$/ console=serial0,115200/' cmdline.txt

    $ echo enable_uart=1 > usercfg.txt

    $ cd ~
    $ umount /mnt/usb
    $ exit

**First Boot:**

.. code-block:: console

    * Insert SD card
    * Connect console cable
    * Connect network cable
    * apply power

    * default loging: root/<blank>

    $ setup-alpine

    $ VERSION="v3.8"

    $ echo "
    http://dl-cdn.alpinelinux.org/alpine/$VERSION/main/
    http://dl-cdn.alpinelinux.org/alpine/$VERSION/community/
    @edge http://nl.alpinelinux.org/alpine/edge/main
    @edgecommunity http://nl.alpinelinux.org/alpine/edge/community
    @testing http://nl.alpinelinux.org/alpine/edge/testing
    " > /etc/apk/repositories

    $ apk update
    $ apk upgrade

    $ apk add nano wget i2c-tools@testing

    $ sed -i '/#PermitRootLogin prohibit-password/c\PermitRootLogin yes' \
        /etc/ssh/sshd_config

    # add private repo key to /etc/apk/keys
    # add private repo urls to /etc/apk/repositories

    $ lbu commit -d

    $ reboot

Raspbian
---------------------------------------

#. `Raspbian <https://downloads.raspberrypi.org/raspbian/images/>`_
#. `Raspbian Lite <https://downloads.raspberrypi.org/raspbian_lite/images/>`_


Community
======================================

#. TBD

Accessories
======================================

#. `USB to TTL Serial Cable <https://www.adafruit.com/product/954>`_
#. `Secure Boot Flash Drive <https://www.sparkfun.com/products/16901>`_


References
======================================

#. `RPI GPIO Pinout <https://forum.pycom.io/topic/1519/power-up-wipy-from-raspberry-pi-3>`_
#. `Using Console Cable <https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/overview>`_
#. `Everything you wanted to know about RPI GPIO <https://www.circuits.dk/everything-about-raspberry-gpio/>`_
#. `Why are Industrial Pis so expensive? <https://youtu.be/9MqJI_F-sz8>`_
