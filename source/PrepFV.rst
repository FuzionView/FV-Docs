Preparing for FuzionView
==========================
Thank you for your interest in being a data provider for the FuzionView project. This document will provide guidance on initial steps you can take to get ready to share your data.


Background
------------
Our project is dedicated to providing the most complete map view of underground utilities. Working with partners like you, we will continue to add facility operators to provide the most complete list of features possible for each 811 ticket. This phase of the project is focused on Minnesota and we have partnered with Gopher State One Call (GSOC) the nonprofit, state-wide utility notification center for excavators, engineers and locators in Minnesota.


Step 1: Data Access
--------------------
FuzionView is designed for maximum flexibility in connecting to your data. The most common connections will be via an ESRI REST server or WFS Service. You’ll want to work with your IT department to create this connection and set up authorization to ensure secure access to the data. Ideally this connection would provide a WFS endpoint with the data in columns as needed, allowing us to perform a one to one transformation on the data. 
Where necessary, we can create a GUI that would allow us to remap some columns, concatenate some columns, do some lookups with a bounded set of options.
In rare circumstances, we could manually transform the data using SQL.

Step 2: Information Needed
----------------------------
FuzionView operates with a small set of required and optional data. During onboarding we will ask you to answer questions that help to define business rules that help us configure your data.

**The required data elements are:**

   * LAYER 
   * PROVIDER_FID 
   * GEOM 
   * STATUS 

**The optional data elements are:** 

   * SIZE
   * DEPTH
   * ACCURACY_VALUE
   * DESCRIPTION. 

Definitions
-------------

**LAYER**
The feature category used to produce the graphical image on the map.

   * Survey
   * Electric
   * OilGasSteam
   * CommCableConduit
   * PotableWaterReclaimedWater
   * SewersDrains
   * Reference

**PROVIDER_FID**

The feature ID, the identifying information for each feature used by your organization. 

**GEOM**

The 3D geometry used to place the feature on the map.

**STATUS**

Indicates how the feature is currently being used.

   * 0 unknown 
   * 1 active 
   * 2 abandoned 
   * 3 planned/under construction
   * 4 removed

**SIZE**

Provided as either a point (with an x/y coordinate) or a line to indicate width and length.

**DEPTH**

Provided as either a point (with an x/y coordinate) or a line to indicate distance from the surface.

**ACCURACY_VALUE**

When provided, indicates the precision used to collect the data.

    * Sub Centimeter
    * Sub Foot
    * Sub Meter
    * Greater Than Meter
    * GeoReferenced/Digitized
    * Hand Drawn

*See the Glossary below for descriptions of each Accuracy Value*

**DESCRIPTION**

Optional text to be displayed to provide additional information.
