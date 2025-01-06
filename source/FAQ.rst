Frequently Asked Questions
============================

Category: Data Creation
-------------------------


**Q:** Are all the Facility Operator fields mandatory?
**A:** No. The first four fields are Required; the others are Optional. If the data is available and provided, it will be displayed. Follow this link to learn more about required and optional fields.


**Q:** What if depth is not stored in our data?
**A:** A separate "DEPTH" data point can also be sent in.  

**Q:** What if we have GPS Points that store the accuracy & depth? For example, when a mainline changes depths throughout, one depth per feature is not an accurate depth for the entire line. 
**A:** The preferred method is to categorize by feature type. See the schema above. In some cases, we may be able to assist with converting the data.


**Q:** Should we combine abandon_mainline & mainline or can we leave them separate?
A: They can be combined or separated.  All features will be grouped by FuzionView engine based on their APWA FEATURE_CLASS color coded infrastructure type.
Ideally they would be combined into one feature category, as long as the STATUS was correctly identified as abandoned or active. 



**Q:** Does the Provider ID need unique numbering? 
**A:** It only needs to be unique by dataset.

**Q:** Should the fields have a text/number classification & is there a standard length?
**A:** Data elements can be alphanumeric, and there is currently no length limitation.  The emphasis should be on providing the data elements in as human readable a format as possible.

**Q:** Do you have an example of Feature 1 or 2 items in a Shapefile so we can use it to configure our data? 
**A:** Follow this link to a GEO PACKAGE with sample data.

Category: Connectivity
-----------------------

**Q:** How do you set up an API key?
**A:** FuzionView needs an API token to connect to most GIS systems. Arc GIS has a good tutorial that is available here: 
https://developers.arcgis.com/documentation/mapping-apis-and-services/security/tutorials/create-and-manage-an-api-key/
You will need an ArcGIS Dev or Arc Online (Creator) account.  There are limitations put on the API creation aspect by ESRI.  

Another potential option is to turn on WFS on your server.  Needs research 



