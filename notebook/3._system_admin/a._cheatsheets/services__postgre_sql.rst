.. _eA-EugTVQy:

=======================================
Postgre SQL
=======================================

General Commands
=======================================

.. code-block:: console

    $ sudo -u postgres -i
    $ psql

    # In PSQL shell
    $ \connect <database>
    $ \dt                                               # list the tables in the current database
    $ \du                                               # list users

    $ \help

    $ \list                                             # List all databases

    $ \password <user_name>                             # default is blank/none

    $ show data_directory;

    $ \quit (\q)


Database Management
=======================================

.. code-block:: sql

    CREATE ROLE <user_name> WITH LOGIN PASSWORD '<password>';       /* create database user */
    ALTER ROLE <user_name> CREATEDB;                                /* Add permission to user_name */

    CREATE DATABASE <db_name> OWNER <user_name>;

    CREATE ROLE <user_name> WITH LOGIN PASSWORD '<password>';       /* create database user */

    GRANT ALL PRIVILEGES ON DATABASE <database> TO <user_name>

    DROP DATABASE [ IF EXISTS ] <db_name>;                          /* Can only be done by db owner [1] */

Notes:

#. IF EXISTS: do not throw an error if the db doesn't exist.



References
=======================================

#. TBD
