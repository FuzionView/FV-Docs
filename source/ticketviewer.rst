Using Ticket Viewer
========================
The FuzionView **Ticket Viewer** displays the polygon for a ticket area as a solid line, surrounded by a 100 foot buffer, shown as a dotted line. When feature information is contributed from a Facility Operator, that data is displayed inside the buffer area as lines and dots.

.. figure:: /_static/TicketViewer1.png
   :alt: The FuzionView Ticket Viewer
   :class: with-border
   
   *FuzionView Ticket Viewer*

.. hint::
   Zoom in to see features at a greater scale. Zoom out to see buildings and infrastructure that surround the ticket area.

Identify Facility Infrastructure
---------------------------------
Hover over a **dot or line** to see highlighted borders around a feature. Click on the feature you want to identify to display the available information. The header shows the Data Provider and Ticket Number, and the feature information provided to FuzionView by the Data Provider:
  * Feature Class
  * Dataset
  * Data Owner
  * Status from 811 system
  * Ticket Number
  * Updated At date and time
  * Description (if provided)
  * Size (if provided)
  

If a feature exists nearby or on top of another feature, those feature IDs will be listed at the bottom as **Nearby Features**. 
See **Stacked Features** below for more information.

.. figure:: /_static/Identify1.png
   :alt: Information about the selected object
   :class: with-border
   
   *Identifying Features*

For definitions for each item of information, check out the `Glossary <https://uumpt.sharedgeo.net/docs/PrepFV.html#definitions-and-schema#>`_

Stacked Features
------------------

Underground utilities are often found above or below other utilities. When you select a feature, if there are other utilities hidden by the selected feature, those feature IDs are listed at the bottom. Simply click through all the **Nearby Features** links to see a complete picture of all the features within the buffer area.

Ticket Info
------------

Click the **Information** icon at the top right to see additional ticket info.

.. figure:: /_static/TicketInfo1.png
   :alt: Ticket Information
   :class: with-border
   
   *Ticket Information*

The **Ticket Info** view has the following tools and information:
   * Ticket Information - Ticket Number and Type.
   * Data Set Providers - the owners who provided the information and the number of features they manage.
   * Options for Downloading the ticket map information. *See the section below on Downloads*
   * Links to the GSOC Ticket and Help. *See the section below on the GSOC Ticket*

**Downloads**

From the Ticket Info window you can select from several **Download Options**:
 * The default **File Type** is GeoJSON. Click the arrow to select a Shapefile or GeoPackage.
 * Select one of the other options to open a Points, Polygons, or Lines file in a new window.

.. figure:: /_static/Downloads1.png
   :alt: Download Options
   :class: with-border
   
   *FuzionView Download Options*

**The GSOC Ticket**

You can open the original GSOC ticket from Ticket Info by clicking **View GSOC Ticket**. 
This is the original ticket in your 811 ticketing system. For more information about GSOC, check out the documentation `here <https://www.gopherstateonecall.org/resources/downloads#iticVideos>`_ 

.. figure:: /_static/GSOC2.png
   :alt: Gopher State One Call
   :class: with-border
   
   *Gopher State One Call (GSOC)*

**Help**

This link opens the FuzionView documentation.

Ticket Layers
--------------

From the Ticket Viewer, select the **Layers** icon at the top right to see available features in each layer. 

.. figure:: /_static/Layers1.png
   :alt: Ticket Layers
   :class: with-border
   
   *Ticket Layers Options*

You can change your view of a ticket by toggling a layer on or off. 

All layers are shown by default. Click any layer to hide it. 

Click again to display it once more. 

Layers with no features will display grayed out.

Basemaps
----------

From the Ticket Viewer, select the **Basemaps** icon at the top right to see available map options. 
* Select **Aerial** to replace the default OpenStreetMap. 

.. figure:: /_static/Basemaps1.png
   :alt: Map Options
   :class: with-border
   
   *Choose Map Option*

Navigation
------------

Use the **Navigation Options** at the bottom left and right to:
 * **Measure** distance or area *See below for more information on using the Measure Tool.
 * **Fit** adjusts the zoom so the ticket boundaries fit in the current window. 
 * **Zoom** to your current location when GPS location is enabled.
 * **Zoom** in (+) and out (-) on the ticket boundaries.
 * The **Scale** displays the size of the ticket boundary in meters and feet.

.. figure:: /_static/Navigation1.png
   :alt: Ticket Viewer Navigation Options
   :class: with-border
   
   *Ticket Viewer Navigation Options*

Measure Tool
--------------

To measure **Distance**, click the Measuring Tool icon and select the Distance option.

.. figure:: /_static/MeasureTool1.png
   :alt: The Measuring Tool
   :class: with-border
   
   *Ticket Viewer Measurement Tools*

Your cursor will become a cross. Click anywhere to create the starting point for the measurement. Click again on the end of the space where you want to measure the distance. You can continue to create distance measurements from the original starting point or double click on the last end point to stop measuring. To clear the measurements and start over, use the refresh button. 

.. figure:: /_static/MeasureTool2.png
   :alt: The Measuring Tool
   :class: with-border
   
   *Distance Measurement Example*

To measure **Area** click the Measuring Tool and select the Area option. Your cursor will once again be changed to a cross. Click at the starting point, then click again at one boundary of the area to be measured. Click again to create a three sided area. Click again to create a four sided area. You can use multiple, small sides to create more circular areas. 

.. figure:: /_static/MeasureTool3.png
   :alt: The Measuring Tool
   :class: with-border
   
   *Area Measurement Example*