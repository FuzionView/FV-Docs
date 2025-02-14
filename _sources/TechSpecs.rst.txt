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
  * Shared Features database schema
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