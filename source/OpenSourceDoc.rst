Developer Documentation
========================

FuzionView documentation is geared towards four audiences:

* **End User Documentation** for homeowners, locators, excavators, and design Engineers who are ticket owners using the FuzionView Ticket Viewer to enhance the information in an 811 dig ticket.
* **Data Provider Documentation** for facility owners and other data providers who need to configure datasets and users to manage their data.
* **System Operator Documentation** for GIS or IT staff at an 811 system provider who need to install, configure, and manage their FuzionView system.
* **Developer Documentation** for anyone who wants to use the FuzionView Core Engine to build a product or extension.
   * **Guide for Developers**: Tips for getting started with the FuzionView Core Engine open source project.
   * **Components**: A high level, visual explanation of a FuzionView system. 
   * **Technical Specifications**: More detailed information about the FuzionView data schema, APIs, and functionality.
   * **Security Specifications**: Provides an understanding of FuzionView's three pronged approach to data security.
   * **Frequently Asked Questions**: A collection of common questions from developers.

FuzionView Engine
==================

FuzionView is built around a PostgreSQL database using the following tools:

*  PostgreSQL has been selected for the database for its open-source nature, reliability and scaleability. 
*  The FuzionView Engine is written in C++, which provides exceptional performance and efficiency.
*  The Boost C++ library has been included to enhance C++ code readability, improve productivity, and increase reliability.
*  FuzionView leverages Apache, the open-source web server software, that can be scaled for high traffic volume.
*  SharedGeo licenses MapServer for interactive map visualizations, because it is highly customizable and supports a variety of data formats.
*  GDAL/OGR (Geospatial Data Abstraction Library) supports multiple coordinate systems and supports GIS visualization of data from multiple sources.
*  PostGIS enables the PostgreSQL database to support geospatial data withing the SQL language.
*  SharedGeo uses the Crow C++ framework as a webserver because of its speed, small footprint, and minimal dependencies.

The tools in the FV-Engine repository manipulate and work with the dbase, focusing on two main categories of activities:

*  Loading
*  Maintenance


Loading
--------

| The **fv-api-server** exposes a REST API used to add new 811 tickets, query existing tickets, mapviews, and features in the FuzionView database. FuzionView queries all datasets for an area of interest (base on GIS location) and aggregates the feature data from various data providers into one features table with a uniform structure.
| **Mapserver** is responsible for providing WMS and WFS views of features to FV-Client and the FuzionView Ticket Viewer. While conceptually **mapserver** lives behind the **fv-api-server**, in implementation it lives behind Apache, which is hidden from the user.

Maintenance
------------

The **db-maint** folder contains two utilities. **archive_stale_tickets** that archives inactve tickets and **update_feature_cache** that looks for tickets that should have datasets. If they do not, this utility runs the query and adds the missing map features to the database. Both utilities run in the background and are not exposed as a webpage. Designed to be able to run on more than one server at a time, so that as the number of datasets grows, and the time to query becomes a limiting factor, multiple servers can be configured to handle the load. 

Ticket Loader
--------------

The FuzionView **ticket_loader** loads new 811 tickets into the system by calling the API to add a ticket. In future, the System Operator would have this capability in their system. FuzionView uses it to load test tickets for FV-Demo. 

The intention is that most of the configuration for FuzionView is in the PostgreSQL database and the other components would pull what they need from there. This may not be complete before the open source release. 

Database
---------

Everything in PostgreSQL lives in the **schema** repository. To create the PostgreSQL database, run 

.. code-block::

   create_users_and_database_example.sql

When complete, use psql to run the necessary schema migrations. Check the readme file to find the latest version. The dates and times in the file name also indicates the migration path from previous version to current version. Example: migrate_20241206111420_20250112022845.sql
If you are mutliple versions back, you will need to run all the migrations in order. Running them out of order will have unpredictable outcomes.


.. warning::

   Do not add to or change the FuzionView schema as it will make future version upgrades impossible.

FV-Demo
--------

FV-Engine is used for the more public components of FuzionView. FV-Admin is kept in a separate respository so that access can be more restricted. Check out the System Operator documentation for more information. 

.. note::

   FV-Demo uses a self-signed certificate for demonstration and testing purposes. 
    
**FV-Demo** has been created to pull all the modules together and allow you to run FuzionView for development or demonstration with a very minimal configuration. Check out the FV-Demo documentation for more details.

Version 1.0 Last Updated: |today|
