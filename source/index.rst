.. FuzionView documentation master file, created by
   sphinx-quickstart on Sat Jan 20 11:09:55 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

FuzionView Documentation
=========================
FuzionView software aggregates all utility location data (GIS) into a single map “on the fly”. This provides engineering design teams, facility operators, locators, excavators and homeowners with an unprecedented view of the underground utilities at the site, providing the opportunity for a safer, more efficient approach to each project. Each map is provided as part of an 811 ticket and is limited to the excavation area, plus a 100 foot buffer. The software is easy for facility operators to implement, and data is only available to authorized users.

This documentation has four audiences:

**End User Documentation** is for homeowners, locators, excavators, and design Engineers who are ticket owners that want to use the FuzionView Ticket Viewer.

**Data Provider Documentation** is for facility owners and other data providers who need to configure datasets and users to manage their data.

**System Operator Documentation** is for the GIS or IT staff at an 811 system operator who need to install and configure the FuzionView system.

**Developer Documentation** is for those who wish to use the FuzionView Core Engine to build their own product.

Use these guides to explore the available functionality. 
If you have feedback, please email info@sharedgeo.org

.. toctree::
   :maxdepth: 99
   :caption: User Documentation

   openfv
   ticketviewer
   FAQ
   
.. toctree::
   :maxdepth: 99
   :caption: Data Provider Documentation
   
   PrepFV
   DataProviderAdmin
   DataProvider
   ConnectToFV
   Components
   TechSpecs
   SecuritySpecs
   FAQ
   
.. toctree::
   :maxdepth: 99
   :caption: System Operator Documentation

   ImplementationGuide
   SystemOperatorAdmin
   SystemOperator
   Components
   TechSpecs
   SecuritySpecs
   FAQ

.. toctree::
   :maxdepth: 99
   :caption: Developer Documentation

   OpenSourceDoc
   DevGuide
   ImplementationGuide
   Components
   TechSpecs
   SecuritySpecs
   FAQ

.. toctree::
   :maxdepth: 99
   :caption: Learn More
   
   About
   
.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
