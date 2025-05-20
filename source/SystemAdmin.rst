System Admin
=============

After logging in, select the System Admin option.

.. figure:: /_static/A-Login1.png
   :alt: Admin Landing Page
   :class: with-border
   
   *Admin Landing Page*

Use the Admin Console to manage:

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
   :class: with-border
   
   *Data Providers*

Add Data Provider
^^^^^^^^^^^^^^^^^^^

Add as many data providers to the system as needed by selecting **Add New Data Provider** from the dropdown menu or the link at the bottom of the page. Enter a clear identifying name and click **Submit**. 

.. figure:: /_static/A-DataProviderNew1.png
   :alt: New Data Provider
   :class: with-border
   
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

.. figure:: /_static/SOAdmin2_DataProviderName1.png
   :alt: Edit Data Provider Name
   :class: with-border
   
   *Edit Data Provider Name*

Delete Data Provider
^^^^^^^^^^^^^^^^^^^^^

To permanently remove a data provide, click the **Trashcan** action icon next to the provider name.

.. warning::
   This cannot be undone.

.. figure:: /_static/SOAdmin7_DeleteDataProvider1.png
   :alt: Delete Data Provider
   :class: with-border
   
   *Delete Data Provider*

Users
------

Once a Data Provider has been added, add a user to securely access and manage their datasets. When created, datasets have no users.

.. figure:: /_static/A-Users0.png
   :alt: Add First User
   :class: with-border
   
   *User Management*

Create User
^^^^^^^^^^^^

Select **New User** to add a user. Enter the email address of the new user and click **Submit**.

.. figure:: /_static/DPAdmin2_Users2.png
   :alt: Create User
   :class: with-border
   
   *Create User*

A confirmation message will display when the user has been created.

.. figure:: /_static/DPAdmin2_Users4.png
   :alt: User Created
   :class: with-border
   
   *User Created*

Manage Users
^^^^^^^^^^^^^

To manage existing users, select the icon next to the user you want to Edit or Delete.

.. figure:: /_static/DPAdmin2_Users3.png
   :alt: Edit or delete existing user
   :class: with-border
   
   *Edit or Delete User*

Datasets
----------

Once the System Operator adds you to FuzionView as a data provider, these actions are available to you:

   * Click the **Eye** icon to view, add, and manage your datasets
   * Click the **Pencil** icon to edit the connection for a dataset
   * Click the **Map** icon to create a test ticket to validate the dataset connection
   * Click the **Trashcan** icon to delete a dataset

Add Dataset
^^^^^^^^^^^^^ 

To add the first dataset, select **New Dataset** and enter the information needed to connect to the dataset:
  * Name
  * Source dataset (the URL for the source ESRI or WFS)
  
Click **Submit** to add the dataset.

.. figure:: /_static/DPAdmin1_NewDataset1.png
   :alt: Add Dataset
   :class: with-border
   
   *Add New Dataset*

Some datasets will require additional information to establish a connection. Click the option for **Basic dataset entry** and add the information needed to connect to your dataset:
  * Name
  * Source dataset (the URL for the source ESRI or WFS)
  * Source SQL
  * Source CO
  * Choose whether to cache the whole dataset
  * Choose whether to enable the dataset (on by default)
  * Source SRS (the EPSG code for the coordinate system in use)
  * Click **Submit** to add the dataset.

.. Note::
   When the dataset is not enabled, the data will only be visible in test tickets used to validate the dataset. 

.. figure:: /_static/DPAdmin1_NewDataset1.png
   :alt: Add Dataset
   :class: with-border
   
   *Add New Dataset*
   
View Datasets
^^^^^^^^^^^^^^^

To view and manage the datasets associated with a Data Provider, click the **Eye** action icon next to the data provider's name. When first created, Data Providers have no datasets.

.. figure:: /_static/DPAdmin1_NoDataset1.png
   :alt: No Datasets 
   :class: with-border
   
   *No Datasets have been added*



Manage Datasets
^^^^^^^^^^^^^^^^^
Select the icon next to a dataset to View, Edit, or Delete it.

.. figure:: /_static/DPAdmin1_Datasets1.png
   :alt: Dataset Management
   :class: with-border
   
   *View, Edit, or Delete Dataset*

.. figure:: /_static/DPAdmin6_Datasets2.png
   :alt: Dataset Management
   :class: with-border
   
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
 
 .. figure:: /_static/DPAdmin10_TestTicket1.png
   :alt: Dataset Validation
   :class: with-border
   
   *Create Test Ticket*

A Pending status message is displayed. It may take up to 5 minutes for the available feature data to populate. 
 
.. figure:: /_static/DPAdmin10_TestTicket2.png
   :alt: Dataset Validation
   :class: with-border
   
   *Create a Test Ticket*

* Once the ticket has been created, the status will update to successful
* Click the Test Ticket link to view the feature data and confirm configuration

.. Note::
   The test ticket is available in the system to any authorized user of the dataset. 
   The ticket exists for only 24 hours and will be automatically deleted.

.. Warning::
    If you select a ticket boundary outside the service area, an error message will be displayed.

.. figure:: /_static/DPAdmin10_TestTicket0.png
   :alt: Test Ticket Warning
   :class: with-border
   
   *Create a Test Ticket*

Service Area
-------------
Data providers can define their service area, which allows FuzionView to optimize service requests. 

Create Service Area
^^^^^^^^^^^^^^^^^^^^

Navigate to Datasets, select the option to **Define a Service Area**.

.. figure:: /_static/DPAdmin11_ServiceArea1.png
   :alt: Dataset Management
   :class: with-border
   
   *Dataset Management*

Draw the Service Area
^^^^^^^^^^^^^^^^^^^^^^

Use the **+** icon on the left to zoom into the correct location. Select the **Polygon** icon on the left and draw a simple shape around the desired area. Use the points in the middle of each line to adjust the shape until it correctly defines your service area. 

.. figure:: /_static/DPAdmin11_ServiceArea3.png
   :alt: Service Area Management
   :class: with-border
   
   *Service Area Management*

Submit Service Area
^^^^^^^^^^^^^^^^^^^^

When the service area is defined as accurately as possible, click the **Submit** button to save. A message will display indicating that the service area has been set.

.. figure:: /_static/DPAdmin11_ServiceArea4.png
   :alt: Submit Service Area
   :class: with-border
   
   *Submit Service Area*

Delete Service Area
^^^^^^^^^^^^^^^^^^^^

If the service area changes, simply delete the existing service area and create a new one. A confirmation will be displayed. Click **OK** to remove the service area.

.. figure:: /_static/DPAdmin11_ServiceArea5.png
   :alt: Delete Service Area
   :class: with-border
   
   *Delete Service Area*

System Settings
----------------

Select **System Settings** from the System Operator menu to manage:

 * Feature Classes
 * Features Status
 * Ticket Types

Use the **Eye** icon to view and edit and the **Plus** icon to create these key elements.

.. figure:: /_static/SOAdmin4_SystemSettings1.png
   :alt: System Settings
   :class: with-border
   
   *System Settings*

Feature Classes
^^^^^^^^^^^^^^^^^

Feature Classes are used to identify a feature category - known as a **LAYER** in Ticket Viewer. 
When a ticket has features in that layer, it will be displayed on the map in a specific color to clearly identify it.
Use the **Pencil** icon to edit and the **Trashcan** icon to delete.

.. figure:: /_static/SOAdmin4_FeatureClasses1.png
   :alt: Feature Classes identify the Layers in FuzionView
   :class: with-border
   
   *Feature Classes*

Add New Feature Class
^^^^^^^^^^^^^^^^^^^^^^^

Scroll to the bottom and select the **Plus** icon or **Add New Feature Class** to identify a new feature class. 
   
.. figure:: /_static/SOAdmin5_NewFeatureClass1.png
   :alt: Add New Feature Classes
   :class: with-border
   
   *Add Feature Class Layers*

Edit Feature Class
^^^^^^^^^^^^^^^^^^^^

Select the **Pencil** icon to edit an existing Feature Class.

.. figure:: /_static/SOAdmin5_EditFeatureClass1.png
   :alt: Add New Feature Classes
   :class: with-border
   
   *Add Feature Class Layers*

Feature Statuses
^^^^^^^^^^^^^^^^^^

Status is used to indicate whether the feature is in use and in what state of development.

.. figure:: /_static/SOAdmin5_FeatureStatuses1.png
   :alt: New Feature Statuses
   :class: with-border
   
   *Feature Statuses*

Add Feature Status
^^^^^^^^^^^^^^^^^^^^

You must create a Feature Status before you configure it. Scroll to the bottom and select **Add New Feature Status** to identify a new usage status:

.. figure:: /_static/SOAdmin6_NewFeatureStatus1.png
   :alt: Add New Feature Status
   :class: with-border
   
   *Add Feature Status* - Placeholder

Edit Feature Status
^^^^^^^^^^^^^^^^^^^^

Click the **Pencil** icon next to a status edit it

.. figure:: /_static/SOAdmin6_EditFeatureStatus1.png
   :alt: Edit Feature Status
   :class: with-border
   
   *Edit Feature Status*

Ticket Types
^^^^^^^^^^^^^

The Ticket Type is used to visually indicate the urgency of a ticket, which is used in planning response time.
The current options are Normal and Emergency. Emergency tickets display with the ticket number in red.

.. figure:: /_static/SOAdmin8_TicketTypes1.png
   :alt: Ticket Types
   :class: with-border
   
   *Ticket Types*

Add a Ticket Type
^^^^^^^^^^^^^^^^^^^

Scroll to the bottom and select **New Ticket Type** to add a new level of urgency.

.. figure:: /_static/SOAdmin8_NewTicketType1.png
   :alt: New Ticket Type
   :class: with-border
   
   *New Ticket Type*

Edit Ticket Type
^^^^^^^^^^^^^^^^^

Click the **Pencil** icon to edit an existing Ticket Type:

.. figure:: /_static/SOAdmin8_EditTicketType1.png
   :alt: Edit Ticket Type
   :class: with-border
   
   *Edit Ticket Type*

Last Updated on |today|
