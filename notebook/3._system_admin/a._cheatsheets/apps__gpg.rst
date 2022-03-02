.. _MCPvuTOdBt:

=======================================
GPG
=======================================

Encrypt & Decrypt
=======================================
.. code-block:: console

    $ gpg --output doc.gpg --encrypt --recipient nosuchuser@nospam.org doc

    $ gpg --output doc --decrypt doc.gpg

    # Tar and encrypt
    tar -jcv -C /path/to/dir . | gpg --encrypt \
                                     --recipient nosuchuser@nospam.org  \
                                     --trust-model always \
                                     --output /path/to/encrypted/archive

**Notes:**

* Recipient public key must be in user GPG keyring
* Matching private key must be in keyring


Key Management
=======================================

**List:**

.. code-block:: console

    $ gpg --list-keys
    $ gpg --list-secret-keys


**New:**

.. code-block:: console

    $ gpg --gen-key


**Export:**

.. code-block:: console

    $ gpg --list-keys
    $ gpg -ao <name>-public.key --export <key-id>

    $ gpg --list-secret-keys
    $ gpg -ao <name>-private.key --export-secret-keys <key-id>

    # key-id: part after 4096R/ from list keys (or equivalent...)

    # ASCII armored public key for copy & pasta
    $ gpg --output mykey.asc --export -a D8FC66D2


**Import:**

.. code-block:: console

    $ gpg --import _something_-public.key
    $ gpg --import _something_-private.key




References
=======================================

#. `Ubuntu Gnu Privacy Guard Howto <https://help.ubuntu.com/community/GnuPrivacyGuardHowto>`_
#. `Using the GNU Privacy Guard <https://www.gnupg.org/documentation/manuals/gnupg/>`_
