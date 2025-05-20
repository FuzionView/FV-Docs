Ticket Viewer
==============


The FuzionView **Ticket Viewer** displays a map with the polygon for your ticket area as a solid line. The ticket boundary is surrounded by a 100 foot buffer, shown as a dotted line. When feature information is contributed from a Facility Operator, that data is displayed inside the ticket and buffer area as lines and dots.

.. figure:: /_static/T-TicketViewer1.png
   :alt: The FuzionView Ticket Viewer
  :class: bordered-figure
   
   *FuzionView Ticket Viewer*

.. hint::
   Zoom in (+) to see features at a greater scale. Zoom out (-) to see buildings and infrastructure that surround the ticket area.

Identify Utility Infrastructure
--------------------------------


Click on a **dot or line** to display the available feature information. 

  * The name of the Data Provider that manages the data
  * Your ticket number 
  * Information on the source of the data:

     * Feature Class - the type of utility
     * Dataset - the name of the shared data source
     * Data Owner - who owns and manages the data
     * Status from the 811 system - such as active, under construction, or abandoned
     * Ticket Number - ticket identifier from GSOC
     * Updated At - date and time the feature was last updated
     * Description (if provided)
     * Size (if provided)

*FuzionView displays the most up to date details available.*  

.. figure:: /_static/T-Identify1.png
   :alt: Information about the selected object
  :class: bordered-figure
   
   *Identifying Features*

The `Glossary <glossary.html>`_ has more information about the FuzionView schema.

Stacked Features
------------------

Underground utilities are often found above or below other utilities. When you select a feature, other utilities may be hidden by the selected feature. All known utilities at or near the selected point or line are listed at the bottom. Simply click through the **Nearby Features** links to see a complete picture of all the known features within the buffer area.

Ticket Information
-------------------

Click the **( i )** icon at the top right to see additional ticket information.

.. figure:: /_static/T-TicketInfo1.png
   :alt: Ticket Information
  :class: bordered-figure
   
   *Ticket Information*

The ticket **information** view displays:
   * Ticket Information - Ticket Number and Type, such as normal, emergency, and more.
   * Dataset Providers - Source of the information and the number of features they provided for this ticket.
   * Download - options data to a file.
   * Links to your GSOC Ticket and FuzionView documentation.

**Downloads**

From ticket Information, you can select from several **Download Options**:
 * The default **File Type** is GeoJSON. Click the arrow to select a Shapefile or GeoPackage instead.
 * Select Points, Polygons, or Lines to open the data in a new tab. Notice the option at the top left to change the format of the data to **Pretty-print**. You can save this file as a .json file.

.. figure:: /_static/T-Downloads1.png
   :alt: Download Options
  :class: bordered-figure
   
   *FuzionView Download Options*

**The GSOC 811 Ticket**

Go back to the original GSOC ticket by clicking **View Ticket**. For help using GSOC, check out their `documentation <https://www.gopherstateonecall.org/resources/downloads#iticVideos>`_ .

.. figure:: /_static/T-GSOC1.png
   :alt: Gopher State One Call
  :class: bordered-figure
   
   *Gopher State One Call (GSOC)*

**Help**

Opens all FuzionView documentation.


Feature Layers
---------------

Select the **Layers** icon under the information icon to manage the features displayed in your map. 

.. figure:: /_static/T-Layers1.png
   :alt: Ticket Layers
  :class: bordered-figure
   
   *Display Layers Option*

Available layers are shown by default with a count for each type. You can remove features by clicking on the layer. Click again to toggle it back on. 

.. hint::
   Layers with no features will display grayed out with the note **no data**.

Basemaps
----------

From the Ticket Viewer, select the **map** icon below the layers icon to change your map. 
The default option is **OpenStreetMap**. 

.. figure:: /_static/T-Basemaps1.png
   :alt: Map Options
  :class: bordered-figure

   *OpenStreetMap*

Select **Aerial** to see a satellite image instead. 

.. figure:: /_static/T-Basemaps2.png
   :alt: Map Options
  :class: bordered-figure

   *OpenStreetMap*

Navigation
------------

Use the tools on the bottom left to:
 * **Measure** distance or area 
 * **Fit** adjusts the zoom so the ticket boundaries fit in the current window 
 * **Zoom** to your current location when you have GPS enabled
 * **Zoom** in (+) and out (-) on the map

.. figure:: /_static/T-NavigationIcons-manual.png
   :alt: Ticket Viewer Map Tools
  :class: bordered-figure
   
   *Ticket Viewer Navigation Options*


Measure Tool
--------------

To measure the distance between two or more points, click the Measurement icon and select the **Distance** option. Your cursor becomes a cross. Click anywhere on the map to create the starting point for your measurement. Click again at the end of the line you want to measure. You can continue to create distance segments by clicking in a new location. 


To measure within a selected polygon area, click the Measurement icon and select the **Area option**. Your cursor will once again be changed to a cross. Click at the starting point for your polygon, then click again at one point of the area to be measured. Click again to create a three sided area. Click again to create a four sided area, and so on. You can use multiple, small sides to create more circular areas.

Double click to stop measuring. To clear a measurement, click the red X to close the popup. 

.. figure:: /_static/T-Measurement1-manual.png
   :alt: Distance and Area measurements
  :class: bordered-figure
   
   *Ticket Viewer Measurements*

Last change: |today|
