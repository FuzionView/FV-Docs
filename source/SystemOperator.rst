System Operator Dashboard
===========================

The System Operator Dashboard allows the system operator to view all their tickets that exist in FuzionView. Tickets can be viewed as a List or a Map.

.. figure:: /_static/SODashboard0_Menu1.png
   :alt: The Ticket List
   :class: with-border
   
   *FuzionView System Operator Dashboard PLACEHOLDER*


Ticket List
------------

Displays a list of all the tickets managed by the System Operator. 

.. figure:: /_static/SODashboard1_TicketList1.png
   :alt: The Ticket List
   :class: with-border
   
   *The Ticket List PLACEHOLDER*

Ticket Map
-----------

Displays a map of all the tickets managed by the System Operator.

.. figure:: /_static/SODashboard2_TicketMap1.png
   :alt: The Ticket Map
   :class: with-border
   
   *The Ticket Map PLACEHOLDER*


System Operator Admin
======================

The System Operator Admin is the FuzionView System management interface. Use the Admin options to manage:
 * Data Providers
 * Datasets
 * Users
 * System Settings

.. figure:: /_static/SOAdmin0_Menu1.png
   :alt: System Operator Admin
   :class: with-border
   
   *System Operator Admin*

Data Providers
--------------

Data Providers displays a list of all the Data Providers or Facility Operators managed by the System Operator. 

**Add Data Provider**
Select either the **Plus** icon or **New Data Provider** at the bottom of the page to add a new data provider.
Enter a name and click **Submit**.

.. figure:: /_static/SOAdmin1_NewDataProvider1.png
   :alt: New Data Provider
   :class: with-border
   
   *New Data Provider*

**Manage Data Providers**

.. hint::
   * Click the **Eye** icon to manage the Datasets configured for a Data Provider
   * Click the **Pencil** icon to edit the name of a Data Provider
   * Click the **Person** icon to manage users for a Data Provider
   * Click the **Trashcan** icon to delete a Data Provider

**Datasets** 
Refer to the Data Provider Admin guide `here <#https://uumpt.sharedgeo.net/docs/DataProvider.html#data-provider-admin#>`_

.. figure:: /_static/SOAdmin2_Datasets1.png
   :alt: Manage Datasests
   :class: with-border
   
   *Manage Datasets*

**Rename Data Provider**
Change the name of a data provider here.

.. figure:: /_static/SOAdmin2_DataProviderName1.png
   :alt: Edit Data Provider Name
   :class: with-border
   
   *Edit Data Provider Name*

**Users** refer to the Data Provider Admin guide `here <#https://uumpt.sharedgeo.net/docs/DataProvider.html#data-provider-admin#>`_

.. figure:: /_static/DPAdmin2_Users4.png
   :alt: Edit Data Provider Name
   :class: with-border
   
   *Edit Data Provider Name*

System Settings
----------------

Use the menu to select **System Operator Admin**:

.. figure:: /_static/AdminMenu1.png
   :alt: The FuzionView System Operator Admin Menu
   :class: with-border
   
   *System Operator Admin Menu*

Then select **System Settings** from the dropdown:

.. figure:: /_static/AdminMenu2.png
   :alt: System Settings Menu
   :class: with-border
   
   *System Operator Admin Menu*

The **System Settings** options are displayed:

.. figure:: /_static/SystemSettings1.png
   :alt: System Operator System Settings
   :class: with-border
   
   *System Settings*

Use the **System Settings** options to create and manage key database elements:

**Feature Classes** 

.. figure:: /_static/FeatureClasses1.png
   :alt: Feature Classes identify the Layers in FuzionView
   :class: with-border
   
   *Feature Classes*

Feature Classes are used to identify a feature category known as a **LAYER** in the Ticket Viewer. 
When a ticket has features in that layer, it is displayed in a specific color to identify them on the map.

   
.. figure:: /_static/Layers1.png
   :alt: Feature Classes map to Layers in FuzionView
   :class: with-border
   
   *Feature Class Layers*

Scroll to the bottom and select **Add New Feature Class** to identify a new feature category. 
   
.. figure:: /_static/NewFeatureClass1.png
   :alt: Add New Feature Classes
   :class: with-border
   
   *Add Feature Class Layers*

A confirmation message will display when complete:
   
.. figure:: /_static/FeatureClassCreated1.png
   :alt: New Feature Class Created
   :class: with-border
   
   *New Feature Class Created*

**Feature Statuses**

Status is used to indicate whether the feature is in use and in what state of development it is.

.. figure:: /_static/FeatureStatuses1.png
   :alt: New Feature Statuses
   :class: with-border
   
   *Add Feature Statuses*

Scroll to the bottom and select **Add New Feature Status** to identify a new usage status:

.. figure:: /_static/NewFeatureClass1.png
   :alt: Add New Feature Status
   :class: with-border
   
   *Add Feature Status* - Placeholder

   **Ticket Types**

The ticket type is used to visually indicate the urgency of a ticket, which is used in planning response time.

.. figure:: /_static/TicketTypes1.png
   :alt: Ticket Types
   :class: with-border
   
   *Ticket Types*

The current options are Normal and Emergency. Emergency tickets display with the ticket number in red.

.. figure:: /_static/TicketTypes1.png
   :alt: Ticket Types
   :class: with-border
   
   *Ticket Types Placeholder*

Scroll to the bottom and select **New Ticket Type** to add a new level of urgency.

.. figure:: /_static/NewTicketType1.png
   :alt: New Ticket Type
   :class: with-border
   
   *New Ticket Type*
