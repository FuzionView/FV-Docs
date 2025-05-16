Glossary
---------

**ACCURACY_VALUE**: 
| Indicates the precision used to collect the data, using the ASCE DCBA standard (38-22, 75-22).

* "sub_centimeter"
* "sub-decimeter"
* "sub_foot"
* "sub_meter"
* "greater_than_meter"
* "georeferenced_digitized"
* "hand_drawn"

**DEPTH**: 
| Provided as either a point (with an x/y coordinate) or a line, to indicate meters below the surface.

**DESCRIPTION**: 
| Optional text to be displayed to provide additional information to the end user.

**FEATURE_CLASS**
| The feature category used to produce the graphical image on the map. These are the allowable values from the APWA uniform color code used to mark underground utilities and excavation sites:  

* White: "proposed_excavation"
* Pink: "survey"
* Red: "electric"
* Yellow: "oil_gas_steam"
* Orange: "comm_cable_conduit"
* Blue: "potable_water"
* Purple: "reclaimed_water"
* Green: "sewers_drains"
* "reference"
 
.. figure:: /_static/APWA_Color_Code.png
   :alt: Standard APWA Colors
   :class: with-border
   
   *APWA Standard Colors*

.. Note::
    The APWA color code is based on the ANSI standard Z53.1 Safety Colors. It's used by public agencies, utilities, contractors, and other groups who participate in ground excavation

**GEOM**
| The 3D geometry used to place the feature on the map. Multi-point, multi-line, and multi-polygon are supported. 

.. Note for Minnesota::
   Geometry values are expected to be convertible to EPSG:6344+5703, NAD83(2011)/UTM 15N, NAVD88 meters.
   
**PROVIDER_FID**
| The feature ID is the identifying information for each feature used by your organization. This is provided by the data owner.

**SIZE**: 
| Provided in meters, as either a point (with an x/y coordinate to indicate diameter) or a line, to indicate width. 

**STATUS**
| Indicates how the feature is currently being used.

* "unknown" 
* "active"
* "abandoned"
* "planned"
* "under_construction"
* "removed"
