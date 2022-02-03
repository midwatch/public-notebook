.. _o6xKtebm3y:

=======================================
MongoDB
=======================================

Management
=======================================

Basic Operations
---------------------------------------

**Connect to mongo container:**

.. code-block:: console

    $ docker exec -it <container id> /bin/bash

    $ docker-compose exec mongo /bin/bash

**Basic Commands:**

.. code-block:: console

    $ mongo

        > db
            test

        > show dbs
            admin
            config
            local
            app_1

        > use app_1

        > show collections
            comm_reports
            logs

        > db.comm_reports.deleteMany({})
            { "acknowledged" : true, "deletedCount" : 5 }

        > db.logs.deleteMany({})
            { "acknowledged" : true, "deletedCount" : 11 }

        > exit
            bye

    $ exit


References
=======================================

#. `MongoDB Manual <https://docs.mongodb.com/manual/>`_
#. `MongoDB Shell <https://docs.mongodb.com/manual/mongo/>`_
