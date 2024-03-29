.. _Y9lunoSbuG:

=======================================
Storage
=======================================

File Systems
=======================================

Btrfs
---------------------------------------

Btrfs is intended to address the lack of pooling, snapshots, checksums, and
integral multi-device spanning in Linux file systems.

The file system's on-disk format has been declared stable in the Linux kernel.

**Features:**

* Copy-on-write
* Btrfs Snapshots
* Built-in RAID support
* Online resizing and defragmentation
* Transparent compression

**References:**

* `Btrfs <https://en.wikipedia.org/wiki/Btrfs>`_
* `Is it better to use Btrfs than EXT4 on a Synology NAS? <https://techunwrapped.com/is-it-better-to-use-btrfs-than-ext4-on-a-synology-nas/>`_


ZFS
---------------------------------------

Unlike most files systems, ZFS combines the features of a file system and a
volume manager. This means that unlike other file systems, ZFS can create a
file system that spans across a series of drives or a pool. Not only that but
you can add storage to a pool by adding another drive. ZFS will handle
partitioning and formatting.

**Features:**

* Pooled storage
* Copy-on-write
* Snapshots
* Data integrity verification and automatic repair
* RAID-Z
* Maximum 16 Exabyte file size
* Maximum 256 Quadrillion Zettabytes storage

**References:**

* `OpenZFS Wiki <https://openzfs.org/wiki/Main_Page>`_
* `What is ZFS? Why are People Crazy About it? <https://itsfoss.com/what-is-zfs/>`_


RAID
=======================================

.. list-table:: Standard RAID Levels
   :header-rows: 1

   * - Level
     - Description
   * - 0
     - Stripping
   * - 1
     - Mirrored
   * - 5
     - Striping with parity
   * - 6
     - Striping with double parity
   * - 10
     - Combining RAID 1 & RAID 0


**References:**

* `RAID <https://www.prepressure.com/library/technology/raid>`_
* `Standard RAID levels <https://en.wikipedia.org/wiki/Standard_RAID_levels>`_
* `Non-standard RAID levels <https://en.wikipedia.org/wiki/Non-standard_RAID_levels>`_


RAID-Z
---------------------------------------

The ZFS filesystem provides RAID-Z, a data/parity distribution scheme similar to
RAID 5, but using dynamic stripe width: every block is its own RAID stripe,
regardless of blocksize, resulting in every RAID-Z write being a full-stripe
write.

**Notes:**

* RAID-Z is a variant of RAID-5.
* When drives are added to the RAID-Z pools, they have to be added in multiples of two.


SHR
---------------------------------------

aka Synology Hybrid RAID

**References:**

* `What is Synology Hybrid RAID (SHR)? <https://kb.synology.com/en-br/DSM/tutorial/What_is_Synology_Hybrid_RAID_SHR>`_
* `What is the difference between SHR and RAID? <https://nascompares.com/2016/07/06/what-is-shr-and-what-is-the-difference-between-synology-hybrid-raid-and-ordinary-raid/>`_


Secure Delete
=======================================

Delete and overwrite hard drives to garuntee that the contents cannot be
recovered.


HDD
---------------------------------------

The shred command overwrites specified files repeatedly to make recovery
extremely difficult to recover.

.. code-block:: console

  $ time shred -vfz /dev/<drive>


**Notes:**

a. It takes about 31 hours/tb when connected via USB3
b. Do not use on SSD disks

**References:**

#. `How to Securely Delete Files on Linux <https://www.howtogeek.com/425232/how-to-securely-delete-files-on-linux/>`_
#. `shred(1) — Linux manual page <https://man7.org/linux/man-pages/man1/shred.1.html>`_


SDD
---------------------------------------

blkdiscard will discard all blocks on the device. Options may be used to modify
this behavior based on range or size.

The "secure erase" is the fastest way to make all content on SSD inaccessible and
it's secure by specification not by accident.

**Notes:**

a. Secure erase and blkdiscard require that the device be connected via a SATA
   controller and is unlikely to work via a USB to PATA/SATA Bridge


**References:**

#. `blkdiscard(8) — Linux manual page <https://man7.org/linux/man-pages/man8/blkdiscard.8.html>`_
#. https://unix.stackexchange.com/questions/593181/is-shred-bad-for-erasing-ssds
#. `ATA Secure Erase <https://ata.wiki.kernel.org/index.php/ATA_Secure_Erase>`_
