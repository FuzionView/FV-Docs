Guide for Developers
=====================

.. Note::
    This is from the readme file in the Git repository FV-Demo. Do we want to modify it at all for the in app documentation?

FV-Demo
--------

This repository contains the files needed to build a Docker image to run the FuzionView demonstration / development build. The configuration here is simplified for ease of getting started in a trusted environment and is not meant for production use. In particular, be aware that default, insecure passwords are used and that the PostgreSQL database is ephemeral as it lives inside the container.

The FV-Demo comes with a "fake" Facility Operator/Data Owner that has fictional features that are located in South-Eastern Dakota County, MN. It also comes with a "fake" ticket loader that randomly generates tickets within the service area of the "fake" features.

The general structure of the FV-Demo is to build one image that contains everything (see Dockerfile) and then use that image to start several containers from that image that encapsulate each part of FuzionView (as defined in docker-compose.yml). Since the target for FV-Demo is demonstration and development, it is assumed that all of the containers will likely be running on one machine and sharing one image keeps the actual on-disk footprint smaller.

containers
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

.. 
    git clone --recurse-submodules git@github.com:FuzionView/FV-Demo 

Pulling (Updating)
-------------------

.. code-block
    git pull --recurse-submodules

Pushing
--------

If pushing changes to the FV-Demo repo, it is recommended to use: 

.. code-block
    git push --recurse-submodules=check 

This will avoid pushing an update to FV-Demo that requires commits that are not yet pushed to the submodules. 

Make this option the default for this repo: 

.. code-block
    git config push.recurseSubmodules check

Make this the default option for all repos:

.. Cocde::
    git config --global push.recurseSubmodules check

Also, note that because submodules checkout a specific commit hash, the submodules will initially be in a detached head state. Before making changes to a submodule, it is likely a good idea to switch to the main branch. 

Example:

.. code-block
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

.. code-block
    cd ../.. # back to FV-Demo
    git add src/FV-Engine
    git commit -m 'Updating FV-Engine to include new changes from ...'
    git push

Docker
-------

Building/Running with Docker

Build
^^^^^^

.. code-block
    DOCKER_BUILDKIT=1 docker-compose build

Start
^^^^^^

.. code-block 
    docker-compose up -d && docker-compose logs -f

Stop
^^^^^^

.. code-block
    docker-compose down -t0

Podman
-------

Building/Running with Podman

Build
^^^^^^

.. code-block
    podman-compose build

Start
^^^^^^

.. code-block
    podman-compose up -d && podman-compose logs -f

Stop
^^^^^^

.. code-block
    podman-compose down -t0

Accessing the FV-Demo
======================

  * Once the containers are running, the FuzionView web interface will be available on https://localhost:4443. 
  * The default username is **demo** and default password is **fv**. 
  * Right now, the FV-Admin interface depends on the SharedGeo Keycloak server and requires a Keycloak account.

PostgreSQL
-----------

The PostgreSQL database inside the container is made available on port 54321. And can be accessed, for example, with:

.. code-block
    psql 'host=localhost port=54321 dbname=fv user=fv_admin password=password'

Shell Access
-------------

Shell access to the various containers is available via the standard Docker/Podman tools. For example:

.. code-block
    docker-compose exec fv-apache-server bash
    podman-compose exec fv-apache-server bash


Notes from meeting with Jim 2/21

FV engine is FV-Engine repo. 
containers are split up to run
In the repo is 
Core of FV is a postgres database. 
There are a set of tools in the fv-engine repo that manipulate and work with dbase to perform the tasks needed by fv.
One of those is: loading 
2 main things:
1. api server - exposes the rest api for querying tickets and mapviews, features from fv dbase and for rest api for addding new tickets to dbase that lives in there. 
Broader picture of things: 
conceptually mapserver lives behind the api server - in implementation lives behind apache (hidden from the user)
Apache is at the top of the Stacked
Based on the need to what to server
Mapserver is responsible for providing wms and wfs views of features that are in the dbase

Client facing as above

second part
db maint folder - 2 utilities - archive stale tickets - goes thru and archives the stale tickets to get out of the active ticket table to improve efficiency

update feature cache - looks for tickets that should have datasets and does the query and adds the map features to the dbase
Both run in the background - not exposed as a webpage - run on server in background - can  run on different servers - 

Eventual plan: 
Update feature cache should be able to run on more than one server at once - as number of datasets grows, time to query is going to be a limiting factor and will require mutliple servers to handle hte load.

An example, not expected in prod:
ticket loader loads new tickets into the system by clling the api to add a ticket. The idea was to have a spot where could translate between OCC example place and what fv needs to load a ticket. Ideally this would be implemented into OCC's system and not nee4ded as a separate component of fv. Different probably for everyone. REight now it is loading fake tickets os the FV-demo has somehting to look at.

Most configuration into postgress so all other components need to talk to dbase and get what they need. that's the goal. not quite there. 

Everything in postgress lives in fv schema - 
to create the postgres dbase - run create users and dbase examplkes under schema/fv schema
then run latest scheam file - date time in file name - check for most recent. Older versions are retained to support suporting to new versions. 

migration files - go from older version to newer versions 
migrate oldversion newversion ex: migrate_20241206111420_20250112022845.sql
need some tooling eventually to make this less manual and more automatically
If you apply in wrong order, could be unpredicable results

run with psql - simple example needed see google results

see screen shorter
psql is a shell for postgres - 


look at the comments in the schema - some are included as comments in the dbase - 
incorporate as a link so it doesn't get out of date.
Mention that readme gets updated and  see that for latest version

run doxagen to run on sql - 

FV engine at its core is about aggregating the feature data from various data providers into a uniform structure. (variety of sources) into a unified 
Area of interest - query all datasets for area of interest (based on GIS location)
pulls into a common schema - mutliple features - one features table
pipes, layers, lights, etc points, polygons, lines - get dropped into a single table and then the fv api server lives in fv engine api extracts that to be vizualized by7 a front end like ticket Viewer


Troubleshoot - use a tool to compare schema with original
Do not add to schema as it will make future version upgrades impossible
Assumes a precondition of previous version. 

fv demo pulls everything together to allow you to run things in a very minimal configuration

if multiple versions back, run all the migrations in order

tech Stack
apache
postgres
mapserver - Open source - OSGeo - we license it
lots of gdal - gdal.org 
wrapper around the ogr component "goodal" other gee-dal 
OGR or ogre is half of gdal - meant to be raster only; ogr meant to be vector - now kind of the same thing because too many with Both

gdal is the overarching project

postgis - component of postgressql - postgis.net

Some libraries that are common things:
boost c++ library to make the language bearable

fv engine is written in c++ 

Brent - fv-admin repo - ruby on rails - has its own apis and user interface components
only do admin functions to keep it very small and more trusted users no public access to this
like occ system level operators and people maintining datasets  - vetted, signed agreement, dont hack usage

if something needs to be more public goes in FV-Engine if provate fv-admin  - so can lock down admin tighter


Crow in the APIs https://crowcpp.org/master/
somewhat of a webserver
crow starts up/gets a port/accepts http requests/routes tell it what code to run based on the request
something_api send it over to crow

example: report + wms  crow = ticket map in ticket Viewer

Dataset configuration 
Source CO - get passed into OGR where it becomes thin wrapper around
sql statement passed into ogr to transform whats comeing from dataaet into the fv schema 
co configuration options - key value paris that get passec into ogr - how it opens/manipulates the dataset

authentication - if requires a user name and password - could put into the source CO - needs to be redone - its an option right now and isn't flexible enough 
go to OGR documentation -for more info
in fv-demo look for example with password
We haven't implemented tokens - 
will do this before release to open source - before we add eden prairie
create a jira ticket - back in slack it is mapped out - find it and create a ticket and prioritize it

cache whole dataset - if you dohn't (default) fv makes a request for each ticket that comes in, requests the area for the ticket and stores it in the feature stash
if on, if on, it doesn't care about tickets, just grabs the whole dataset

Caching whole dataset is substantially less server load for us and them  0- like once a week pulls it all versus 1000s of requests per ticket
But most people are sensitive about sharing all their data and want to limit it to just ticket boundary (and buffer)

Enable - determines whether or not the dataset will be considered when a new ticket comes in, ecxept test tickets which are active for 24 hours. Off by default. check with brent on timing. They don't show up in other listings.

srs - special reference system - for example epsg code - update docs
gets passed to OGR - this is a GIS concept - ex: 3,4 where is that on earth? how do we translate that to a location
we need to know what it is in so we can convert it 

point of service area is to not query datasets that we know wohn't have data
query datasets with data
exclude things that will return nothing to save overhead
if too small - will ecxlude real data
if too big - efficiency hint
because of sensitivities - FOs seem more upset about this than actual feature data

ask brent about limiting access to datasets based on defined users
should have to be on the dataset to manage them

start.html to get back to the menu

keep out! - is just a fail authentication test

ask brent about system profile

accuracy classes - define value from what is coming in - domain tables
features table there is an accuracy class/field - has to be one of these values under id - changing or removing them from a live system will invalidate tickets and features classes

ticket types have to match up with the domain list for that ticket type

Likely adding (Brent) is adding key value table for system config - 
- what is logout url , etc from the list
what is the refresh interval (or might add that per dataset)

 













