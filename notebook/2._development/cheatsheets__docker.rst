.. _b0MI2ouTvZ:

=======================================
Docker
=======================================

Build Images
=======================================

.. code-block:: console

    $ docker built -t <container_name>
    $ docker tag <container_name> <username>/<image_name>:tag
        > docker tag friendlyhello john/get-started:part2

    $ docker login -u <username>
    $ docker push <username>/<image_name>


Installation
=======================================

Ubuntu
---------------------------------------

.. code-block:: console

    $ sudo apt-get update

    $ sudo apt-get install -y \
               apt-transport-https \
               ca-certificates \
               curl \
               software-properties-common

    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    $ sudo add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) \
        stable"

    $ sudo apt-get update && sudo apt-get install -y docker-ce

    $ sudo usermod -aG docker $USER                     # logout & backin

    $ docker run --rm hello-world                       # Test docker install

Management
=======================================

Basic Commands
---------------------------------------

**Docker:**

.. code-block:: console

    $ docker run hello-world                            # Pull image from registry and run
    $ docker run --rm hello-world                       # As above but cleans up container on exit

    $ docker search ubuntu

    $ docker pull ubuntu                                # Download ubuntu image
    $ docker inspect ubuntu                             # Inspect ubuntu container

    $ docker ps                                         # List active containers
    $ docker ps -l                                      # List all containers

    $ docker run <container_name>                       # Run container in foreground
    $ docker run -it <container_name>                   # Run container and enter interactive shell
    $ docker run -p 8000:80 <container_name>            # Run container in foreground & map ports [1]
    $ docker run -d <container_name>                    # Run container in detached mode

    $ docker stop <container_id>

Notes:

#. Map host port 8000 to container port 80

**Docker Compose:**

.. code-block:: yaml

    # docker-compose.yaml

    version: '3'

    services:
      devpi:

      jenkins:

      moin:

      nginx:

    volumes:

.. code-block:: console

    $ docker-compose start <service_name>
        > docker-compose start nginx

    $ docker-compose stop <service_name>
        > docker-compose stop nginx

Notes:

#. docker-compose commands must be run in same dir as docker-compose.yaml


Docker Machine
=======================================

Docker machine enables the creation of docker hosts on remote machines and working with them
as if they were a local machine; including running commands via ssh.

.. code-block:: console

    $ eval $(docker-machine env <machine name> )    # set required env vars

    $ docker-machine ls

    $ docker-machine ssh <machine name> <command>
    $ docker-machine scp <command>

    $ docker-machine ssh <machine name>             # Interactive shell

    $ docker-machine rm --force <machine name>      # Destroy remote host

    $ eval "$(docker-machine env -u)"               # Clear env vars


Notes:

#. Connection credentials will be on the initiating machine only ($HOME/.docker/machine/machines/$MACHINE_NAME)


Installation
---------------------------------------

.. code-block:: console

    $ DM_VER="0.16.2"
    $ DM_URL="https://github.com/docker/machine/releases/download/v${DM_VER}/docker-machine-`uname -s`-`uname -m`"
    $ curl -L $DM_URL > /tmp/docker-machine && \
        chmod +x /tmp/docker-machine && \
        sudo mv /tmp/docker-machine /usr/local/bin/docker-machine

Run on Digital Ocean Droplet
---------------------------------------

.. code-block:: console

    $ DO_TOKEN="<token>"
    $ APP_NAME="youtube-history"
    $ MACHINE_NAME=$APP_NAME
    $ IMAGE_NAME="ubuntu-18-04-x64"
    $ DATA_IN_DIR="stage/in"
    $ DATA_OUT_DIR="stage/out"

    # Create droplet
    # =====================================================
    $ docker-machine create \
                     --driver digitalocean \
                     --digitalocean-access-token $DO_TOKEN \
                     --digitalocean-image $IMAGE_NAME \
                     $MACHINE_NAME

    # Stage working files
    # =====================================================
    $ docker-machine ssh $MACHINE_NAME mkdir -p /data/{out,work}
    $ docker-machine scp -r $DATA_IN_DIR $MACHINE_NAME:/data/in


    # Run job
    # =====================================================
    $ eval $(docker-machine env $MACHINE_NAME)
    $ docker build -t $APP_NAME src
    $ docker run --detach \
                 --mount type=bind,src=/data,dst=/data \
                 $APP_NAME

    $ docker logs -f <container id>

    # Get results and destroy machine
    # =====================================================
    $ docker-machine scp $MACHINE_NAME:/data/out/* $DATA_OUT_DIR
    $ docker-machine rm --force $MACHINE_NAME
    $ eval "$(docker-machine env -u)"

Notes:

#.  Running container in background (via --detatch) and tailing the logs will allow task to continue if your local machine disconnects.


References
=======================================

#. `Install Docker CE <https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-repository>`_
#. `Docker Compose Cheat Sheet <https://devhints.io/docker-compose>`_
