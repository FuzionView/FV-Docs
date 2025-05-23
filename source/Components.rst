FuzionView Components
======================

.. Note::
    This is a placeholder until the content can be reviewed and finalized.

FuzionView is an open source application that leverages the power of APIs to collect data quickly and securely to create a more complete picture of a dig area, driving increased awareness of underground utilities, faster locations, and safer excavations. 

Primary features of FuzionView include:
  * Visual identification of underground utilities and other features within the boundary of an 811 ticket
  * Ability to turn different features on or off to create a custom view of the ticket area
  * Option to select between aerial satellite imagery or the streets and structures of an OpenStreetMap
  * A suite of tools that allow you to manage your view of the ticket area, see detailed ticket information, and measure distance and area by drawing lines and polygons.

Admin features include:
  * Ability to add and manage data providers such as facility operators
  * Tools to help you add and validate datasets for each data provider
  * Authorization tools to control access to each datasets
  * System configuration options to customize feature classes, status options, and ticket types.


.. figure:: /_static/components.png
   :alt: FuzionView System  Components
   :class: bordered-figure
   
   *FuzionView System Overview*


About this graphic:
The 811 ticket originates from the Minnesota Gopher State One Call service, managed by OCC. XML data is pushed to FuzionView core engine which initiates a request for data from established data connections. This information is collected and compiled into a features map that can be viewed and manipulated in the FuzionView Ticket Viewer. System Operators can add new data providers, data providers can add new datasets and authorize access to their data.

The FuzionView engine has the following components:

  * fv-db-maint: Database maintenance. Purges out of date tickets and fetches features into the feature cache.
  * fv-ticket-loader: Creates new tickets randomly within the FV-Demo sample data area.
  * fv-api-server: API server for https://localhost:4443/api/....
  * fv-apache-server: Hosts the static web content, the Rails admin tool (https://localhost:4443/admin/...), and MapServer. Also responsible for SSL and most authorization.
  * postgres: The PostgreSQL/PostGIS database that ties everything together.
  
FuzionView is tested to work with Docker and Podman, and on x86-64 and aarch64 (arm64).


Last Updated: |today|
