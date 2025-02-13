Developer Documentation
========================

Audience
---------

FuzionView documentation is geared towards four audiences:

* End User Documentation is for homeowners, locators, excavators, and design Engineers who are ticket owners that want to use the FuzionView Ticket Viewer.
* Data Provider Documentation is for facility owners and other data providers who need to configure datasets and users to manage their data.
* System Operator Documentation is for the GIS or IT staff at an 811 system operator who need to install and configure the FuzionView system.
* Developer Documentation (this document) is for those who wish to use the FuzionView Core Engine to build their own product.

This document focuses on providing a quickstart for developers and utilizes the FuzionView docker image for serving the demo data and code. 
 
   * **Guide for Developers**: Tips for getting started with the FuzionView Core Engine open source project.
   * **Components**: A visual explanation of a FuzionView system. 
   * **Technical Specifications**: More detailed information about the FuzionView data schema, APIs, and functionality.
   * **Security Specifications**: Provides an understanding of FuzionView's three pronged approach to data security.
   * **Technical Implementation Guide**: Explains the basics of installation, setup and configuration.
   * **Frequently Asked Questions**: A collection of common questions from developers.

Basic Requirements
-------------------

  * Git 
  * Docker or Podman 
  * MacOs install tool such as homebrew, npm, etc 

Clone the Repository
---------------------

  This will download the code and sample data to get you started.

  ..code::
   cd ~
   mkdir FV-Engine
   cd FV-Engine
   git clone https://github.com/FuzionView/FV-Demo
   build


