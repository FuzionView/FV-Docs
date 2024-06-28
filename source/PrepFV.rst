Preparing for FuzionView
==========================

Thank you for your interest in being a data provider for the FuzionView project. This document will provide guidance on initial steps you can take to get ready to share your data.


Background
------------

Our project is dedicated to providing the most complete map view of underground utilities. Working with partners like you, we will continue to add facility operators to provide the most complete list of features possible for each 811 ticket. This phase of the project is focused on Minnesota and we have partnered with Gopher State One Call (GSOC) the nonprofit, state-wide utility notification center for excavators, engineers and locators in Minnesota.

Onboarding process
-------------------

In general, these are the steps that will typically occur as you move through the onboarding process:
 * Your organization contacts FuzionView and expresses interest in providing data to FuzionView that will augement the 811 ticket process.
 * A representative from your organization reads the Getting Started with FuzionView document. (You are here!)
 * The decision makers in your organization will attend a demo of FuzionView.
 * Any concerns or questions from your organization have been satisfactorily resolved.
 * Your legal department has confirmed there are no legal barriers such as legislation (either current or pending) that would prohibit providing data to FuzionView.
 * Your organization has designated a primary point of contact to work with FuzionView.
 * The point of contact for your organization is assigned a FuzionView account for evaluation.
 * The point of contact at your organization has read the documentation and attended the training for FuzionView.
 * Your IT department understands the requirements and is prepared to work with the FuzionView team to complete configuration.
 * The required legal agreements have been duly authorized by your organization.
 * Your IT team follows the guide and establishes a connection to share data.
 * Your IT team works with the FuzionView team to configure your datasets and users.
 * Your organization goes live with FuzionView!

Step 1: Data Access
--------------------

FuzionView is designed for maximum flexibility in connecting to your data. The most common connections will be via an ESRI REST server or WFS Service. You’ll want to work with your IT department to create this connection and set up authorization to ensure secure access to the data. Ideally this connection would provide a WFS endpoint with the data in columns as needed, allowing us to perform a one to one transformation on the data. 
Where necessary, we can create a GUI that would allow us to remap some columns, concatenate some columns, do some lookups with a bounded set of options.
In rare circumstances, we could manually transform the data using SQL.

Step 2: Information Needed
----------------------------

FuzionView operates with a small set of required and optional data. During onboarding we will ask you to answer questions that help to define business rules that help us configure your data.

The required data elements are:
 * LAYER 
 * PROVIDER_FID 
 * GEOM 
 * STATUS 

The optional data elements are:
 * SIZE
 * DEPTH
 * ACCURACY_VALUE
 * DESCRIPTION. 

Definitions and Schema
-----------------------

LAYER: The feature category used to produce the graphical image on the map.

* Survey
* Electric
* OilGasSteam
* CommCableConduit
* PotableWaterReclaimedWater
* SewersDrains
* Reference

PROVIDER_FID: The feature ID is the identifying information for each feature used by your organization. 

GEOM: The 3D geometry used to place the feature on the map.

STATUS: Indicates how the feature is currently being used.

* 0 unknown 
* 1 active 
* 2 abandoned 
* 3 planned/under construction
* 4 removed

SIZE: Provided as either a point (with an x/y coordinate) or a line to indicate width and length.

DEPTH: Provided as either a point (with an x/y coordinate) or a line to indicate distance from the surface.

ACCURACY_VALUE: When provided, indicates the precision used to collect the data.

* Sub Centimeter
* Sub Foot
* Sub Meter
* Greater Than Meter
* GeoReferenced/Digitized
* Hand Drawn

DESCRIPTION: Optional text to be displayed to provide additional information.

*See the Glossary for more detailed descriptions.*

Connection Information
-----------------------
After your organization commits to providing data to FuzionView, we will begin collecting the information necessary to connect to your data source. If possible, you should begin collecting this data to help streamline the onboarding process.
