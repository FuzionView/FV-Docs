Technical Specifications
=========================

.. Note::
    This is a placeholder until the content can be reviewed and finalized.

FuzionView uses data and services from a wide variety of sources to create an augmented view of an 811 dig ticket. Sources may include:
  * Feature data providers such as facility operators who provide GIS feature data and attributes, using WFS and ESRI
  * Ancillary data such as Survey Markets, Railroad right of way and, in the future, parcels. 
  * Basemaps from OpenStreetMaps, ArcGIS Test Aerials
  * Future capabilities may include excavator tools for field data collection and 3-D/AR visualization. 

FuzionView components include:
  * Core Engine
  * Shared Features database schema using PostgreSQL
  * User identity management database
  * Data transfer APIs

Optional companion tools:
  * Web Based Ticket Viewer (Leaflet)
  * Web based Data Providers and System Administration interface (Ruby)

Authorization Management:
  * Designed to work with any OpenID based authentication system
  * KeyCloak example configurations included

Basemap Services:
Most online GIS service portals can be used as background map engines. Suggested background layers for use in FuzionView:
  * Aerial Photo
  * Street Centerline
  * Hazardous material locations
  * Restricted Use Area
  * Sensitive/Protective plantings

Available Support:
  * Documentation
  * Deployment and Configuration Tools
  * Hosting Services
  * FuzionView Onboarding


  Front End
  React Typescript
  Leaflet is the main mapping technology used
  OpenStreet map is hosted by SharedGeo - managed service (ask Jim/Bob re: update schedule)
  Front end calls sharedgeo apis: tickets api, report json - homemade webmap services - Bob and Jim set up mapserver - check geospatial data into - creates an api against the geospacial features. Basemap tiles come through mapserver, ex: ticket geometry - give it a feature ID - 
  Front end doesn't call externally 
  
  ES Lint - linting tool
  Vite - run locally and point to external api's
  check code into github 
  setup docker for local instance of database for validating

  Bundle up html, javascript and typescript and hands it off to jim's engine
  
