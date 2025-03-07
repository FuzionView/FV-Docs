Guide to FV-Demo
=====================

This repository contains the files needed to build a Docker image to run the FuzionView demonstration / development build. The configuration here is simplified for ease of getting started in a trusted environment and is not meant for production use. In particular, be aware that default, insecure passwords are used and that the PostgreSQL database is ephemeral as it lives inside the container.

The FV-Demo comes with a "fake" Facility Operator/Data Owner that has fictional features that are located in South-Eastern Dakota County, MN. It also comes with a "fake" ticket loader that randomly generates tickets within the service area of the "fake" features.

The general structure of the FV-Demo is to build one image that contains everything (see Dockerfile) and then use that image to start several containers from that image that encapsulate each part of FuzionView (as defined in docker-compose.yml). Since the target for FV-Demo is demonstration and development, it is assumed that all of the containers will likely be running on one machine and sharing one image keeps the actual on-disk footprint smaller.

Containers
-----------

FV-Demo consists of the following containers:

  * fv-db-maint: Database maintenance. Purges out of date tickets and fetches features into the feature cache.
  * fv-ticket-loader: Creates new tickets randomly within the FV-Demo sample data area.
  * fv-api-server: API server for https://localhost:4443/api/....
  * fv-apache-server: Hosts the static web content, the Rails admin tool (https://localhost:4443/admin/...), and MapServer. Also responsible for SSL and most authorization.
  * postgres: The PostgreSQL/PostGIS database that ties everything together.

FV-Demo is tested to work with Docker and Podman, and on x86-64 and aarch64 (arm64).

Git Notes
----------

Be aware that this repository uses git submodules to pull in the various parts of FuzionView needed to build the Docker image.

Cloning
--------

.. code-block::
    git clone --recurse-submodules git@github.com:FuzionView/FV-Demo 

Pulling (Updating)
-------------------

.. code-block::
    git pull --recurse-submodules

Pushing
--------

If pushing changes to the FV-Demo repo, it is recommended to use: 

.. code-block::
    git push --recurse-submodules=check 

This will avoid pushing an update to FV-Demo that requires commits that are not yet pushed to the submodules. 

Make this option the default for this repo: 

.. code-block::
    git config push.recurseSubmodules check

Make this the default option for all repos:

.. code-block::
    git config --global push.recurseSubmodules check

Also, note that because submodules checkout a specific commit hash, the submodules will initially be in a detached head state. Before making changes to a submodule, it is likely a good idea to switch to the main branch. 

Example:

.. code-block::
    cd src/FV-Engine
    git checkout main
    ... work ...
    git add ...
    git commit
    git push

Then work within that submodule normally, potentially rebuilding and testing the Docker image, and committing and pushing the work to the submodule. 

Update FV-Demo
---------------

To update FV-Demo to use the new version of the submodule git add it and commit, and push. 

Example:

.. code-block::
    cd ../.. # back to FV-Demo
    git add src/FV-Engine
    git commit -m 'Updating FV-Engine to include new changes from ...'
    git push

Docker
-------

Building/Running with Docker

Build
^^^^^^

.. code-block::
    DOCKER_BUILDKIT=1 docker-compose build

Start
^^^^^^

.. code-block:: 
    docker-compose up -d && docker-compose logs -f

Stop
^^^^^^

.. code-block::
    docker-compose down -t0

Podman
-------

Building/Running with Podman

Build
^^^^^^

.. code-block::
    podman-compose build

Start
^^^^^^

.. code-block::
    podman-compose up -d && podman-compose logs -f

Stop
^^^^^^

.. code-block::
    podman-compose down -t0

Accessing the FV-Demo
======================

  * Once the containers are running, the FuzionView web interface will be available on https://localhost:4443. 
  * The default username is **demo** and default password is **fv**. 
  * Right now, the FV-Admin interface depends on the SharedGeo Keycloak server and requires a Keycloak account.

PostgreSQL
-----------

The PostgreSQL database inside the container is made available on port 54321. And can be accessed, for example, with:

.. code-block::
    psql 'host=localhost port=54321 dbname=fv user=fv_admin password=password'

Shell Access
-------------

Shell access to the various containers is available via the standard Docker/Podman tools. For example:

.. code-block::
    docker-compose exec fv-apache-server bash
    podman-compose exec fv-apache-server bash
