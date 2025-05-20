System Administration
======================

Use the tools in System Admin to manage:

+ :ref:`Data Providers`
+ :ref:`Users`
+ :ref:`Datasets`
+ :ref:`System Settings`

.. figure:: /_static/A-Login2.png
   :alt: System Operator Admin
   :class: bordered-figure
   
   *System Operator Menu*

Data Providers
---------------

The **Data Providers** page displays a list of all the facility operators and other data providers you've added to the system.

.. figure:: /_static/A-DataProviders1.png
   :alt: Data Providers
   :class: bordered-figure
   
   *Data Providers*

Add Data Provider
^^^^^^^^^^^^^^^^^^^

Add as many data providers to the system as needed by selecting **Add New Data Provider** from the dropdown menu or the link at the bottom of the page. Enter a clear identifying name and click **Submit**. 

.. figure:: /_static/A-DataProviderNew1.png
   :alt: New Data Provider
   :class: bordered-figure
   
   *New Data Provider*

Manage Data Providers
^^^^^^^^^^^^^^^^^^^^^^^

.. hint::
   * Click the **Eye** action icon to view and manage the Datasets configured for a Data Provider
   * Click the **Pencil** action icon to edit the name of a Data Provider
   * Click the **Person** action icon to manage users with access to a Data Provider
   * Click the **Trashcan** action icon to delete a Data Provider

Rename Data Provider
^^^^^^^^^^^^^^^^^^^^^^

Change the name of a data provider from the Data Providers list by clicking the **Pencil** action icon next to the provider's information:

.. figure:: /_static/A-DataProviderName.png
   :alt: Edit Data Provider Name
   :class: bordered-figure
   
   *Edit Data Provider Name*

Delete Data Provider
^^^^^^^^^^^^^^^^^^^^^

To permanently remove a data provider, click the **Trashcan** action icon next to the provider name.

.. warning::
   This cannot be undone.

.. figure:: /_static/A-DataProviderDelete.png
   :alt: Delete Data Provider
   :class: bordered-figure
   
   *Delete Data Provider*

Users
------

Once a Data Provider has been added, add datasets and a user who can securely manage their datasets. 

.. figure:: /_static/A-Users0.png
   :alt: Add First User
   :class: bordered-figure
   
   *User Management*

Create User
^^^^^^^^^^^^

Select **New User** to add a user. Enter the email address of the new user and click **Submit**.

.. figure:: /_static/A-Users1.png
   :alt: Create User
   :class: bordered-figure
   
   *Create User*

A confirmation message will display when the user has been created.

.. figure:: /_static/A-Users2.png
   :alt: User Created
   :class: bordered-figure
   
   *User Created*

Manage Users
^^^^^^^^^^^^^

To manage existing users, select the pencil or trashcan action icon next to the user you want to edit or delete.

.. figure:: /_static/A-Users2.png
   :alt: Edit or delete existing user
   :class: bordered-figure
   
   *Edit or Delete User*

Datasets
----------

Once a data provider is added, these are the actions available:

   * Click the **Eye** icon to view, add, and manage datasets
   * Click the **Pencil** icon to edit the connection for a dataset
   * Click the **Map** icon to create a test ticket to validate the dataset connection
   * Click the **Trashcan** icon to delete a dataset

View Datasets
^^^^^^^^^^^^^^^

To view and manage the datasets associated with a Data Provider, click the **Eye** action icon next to the data provider's name. When first created, Data Providers have no datasets.

.. figure:: /_static/DPAdmin1_NoDataset1.png
   :alt: No Datasets 
   :class: bordered-figure
   
   *No Datasets have been added*

Add Dataset - Quick Add
^^^^^^^^^^^^^^^^^^^^^^^^

To add the first dataset, select **New Dataset** and enter the name and URL of your dataset. ESRIJSON and WFS are supported. Use a 'WFS:' prefix before WFS dataset urls. ESRIJSON sources should start with 'ESRIJSON:'.
  * Name
  * Credential: No authentication required
  * Source dataset (the URL for the source ESRI or WFS)
  
Click **Submit** to add the dataset.

.. figure:: /_static/A-Dataset2.png
   :alt: Add Dataset
   :class: bordered-figure
   
   *Add New Dataset*

Add Dataset - Basic Entry
^^^^^^^^^^^^^^^^^^^^^^^^^^

Some datasets can be entered with minimal validation. Click the option for **Basic dataset entry** and add the information needed to connect to your dataset:
  * Name
  * Source dataset URL: external link to an externally managed and hosted dataset.
  * Source SQL: command line options that can be passed to gDal.
  * Source CO: describes how the source dataset is stored.
  * Cache the whole dataset: When enabled, operates against the local copy, a good choice for datasets that change infrequently.
  * Enable the dataset: On by default.
  * Source SRS: the EPSG code for the coordinate system in use.
  * Click **Submit** to add the dataset.

.. Note::
   When the dataset is not enabled, the data is only visible in test tickets to validate the dataset. 

.. figure:: /_static/A-Dataset3.png
   :alt: Add Dataset
   :class: bordered-figure
   
   *Add New Dataset*
   

Manage Datasets
^^^^^^^^^^^^^^^^^
Select the icon next to a dataset to View, Edit, or Delete it.

.. figure:: /_static/DPAdmin1_Datasets1.png
   :alt: Dataset Management
   :class: bordered-figure
   
   *View, Edit, or Delete Dataset*

.. figure:: /_static/DPAdmin6_Datasets2.png
   :alt: Dataset Management
   :class: bordered-figure
   
   *View, Edit, or Delete Dataset*

.. Warning::
   When a dataset is modified, the original data will remain in the system until related tickets expire.

Validate Dataset
^^^^^^^^^^^^^^^^^^
Select the **map** action icon next to a dataset to create a test ticket. Use the test ticket to validate that your dataset connection is successful.
 * Select a Data Provider
 * Select a Dataset
 * Click the Map icon
 * Use the Zoom icons to find a test ticket location
 * Select the Polygon tool icon and draw the ticket boundary
 * Click Submit
 
 .. figure:: /_static/DA-TestTicketManual.png
   :alt: Dataset Validation
   :class: bordered-figure
   
   *Create Test Ticket*

* A Pending status message is displayed. It may take up to 5 minutes for the available feature data to populate. 
* Once the ticket has been created, the status will update to successful.
* Click the Test Ticket link to view the feature data and confirm configuration was successful.

.. Note::
   The test ticket is available in the system to any authorized dataset user. 
   The ticket exists for only 24 hours and will be automatically deleted.

.. Warning::
    If you select a ticket boundary outside the service area, an error message will be displayed.

Service Area
-------------
Data providers can define a service area, which allows FuzionView to optimize service requests. 

Create Service Area
^^^^^^^^^^^^^^^^^^^^

Navigate to Datasets, select the option to **Define a Service Area**.

.. figure:: /_static/A-ServiceAreaManual.png
   :alt: Define a Service Area
   :class: bordered-figure
   
   *Define a Service Area*

* Use the **+** icon on the left to zoom into the correct location. Select the **Polygon** icon on the left and draw a simple shape around the desired area. Use the points in the middle of each line to adjust the shape until it defines your service area as closely as possible.

* Click the **Submit** button to save. A message will display indicating that the service area has been set.

Delete Service Area
^^^^^^^^^^^^^^^^^^^^

If the service area changes, simply delete the existing service area and create a new one. A confirmation will be displayed. Click **OK** to remove the service area.

System Settings
----------------

Select **System Settings** from the System Operator menu to manage:

 * Feature Accuracy Classes
 * Feature Classes
 * Features Status
 * Ticket Types

Use the **Eye** icon to view and edit and the **+** icon to add a new object.

.. figure:: /_static/A-SystemSettings2.png
   :alt: System Settings
   :class: bordered-figure
   
   *System Settings*

Feature Accuracy Classes
^^^^^^^^^^^^^^^^^^^^^^^^^

Feature Accuracy Classes are used to indicate how the data was collected as an indication of how reliably accurate it may be. These are the default values you can use to map to any accuracy values you may have set for your data:
 * sub_centimeter
 * sub-decimeter
 * sub_foot
 * sub_meter
 * greater_than_meter
 * georeferenced_digitized
 * hand_drawn

Use the **Pencil** icon to edit or the **Trashcan** icon to delete a value.

.. figure:: /_static/A-SS-AccuracyClass1.png
   :alt: Feature Accuracy Classes
   :class: bordered-figure
   
   *Feature Accuracy Classes*
   
Feature Classes
^^^^^^^^^^^^^^^^^

Feature Classes are used to identify a feature category - known as a **LAYER** in Ticket Viewer. 
When a ticket has features in that layer, it will be displayed on the map in a specific color to clearly identify it.

.. figure:: /_static/A-SS-FeatureClasses1.png
   :alt: Feature Classes identify the Layers in FuzionView
   :class: bordered-figure
   
   *Feature Classes*

 * Use the **Pencil** icon to edit and the **Trashcan** icon to delete class.
 * Select the **Plus** icon or **Add New Feature Class** to create a class.
 * Select the **Pencil** icon to edit an existing class.

Feature Statuses
^^^^^^^^^^^^^^^^^^

Status is used to indicate whether the feature is in use and in what state of development.

.. figure:: /_static/A-SS-FeatureStatus1.png
   :alt: New Feature Statuses
   :class: bordered-figure
   
   *Feature Statuses*

 * Scroll to the bottom and select **Add New Feature Status** to identify a new usage status.
 * Click the **Pencil** icon next to a status edit it.
 Click the **Trashcan** icon next to a status to remove it.

Ticket Types
^^^^^^^^^^^^^

The Ticket Type is used to visually indicate the urgency of a ticket, which is used in planning response time, such as Normal and Emergency. Emergency tickets display with the ticket number in red. The default values are from your state 811 system.

.. figure:: /_static/A-SS-TicketTypes1.png
   :alt: Ticket Types
   :class: bordered-figure
   
   *Ticket Types*

 * Select **New Ticket Type** to add a new type.
 * Click the **Pencil** icon to edit an existing Ticket Type:

Last Updated on |today|
