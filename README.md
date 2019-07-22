# CS-5010-Project
Charlottesville Real Estate

# Links
Dataset Website: https://opendata.charlottesville.org
- Real Estate (base data) https://opendata.charlottesville.org/datasets/real-estate-base-data
- Real Estate (sales) https://opendata.charlottesville.org/datasets/real-estate-sales

# Data
Real Estate (base data)
15,558 Records
This data set includes information pertaining to the transfer (sales) history for parcels. The "ParcelNumber" field can be joined to the "ParcelNumber" field in the "Parcel Area Details" data set for mapping purposes (current parcels only).This dataset is updated on a daily basis and reflects the Real Estate system as of the previous business day. The assessment values are done yearly and reassessment notices go out at the end of January.

Real Estate (sales)
54,347 Records
Real Estate Information - Parcel Level Data.  Only active parcels are included in this data set.  The "ParcelNumber" field can be joined to the "ParcelNumber" field in the "Parcel Area Details" data set for mapping purposes. Please refer to this Data Guide for details on how to access and join Real Estate data

Related Data
- Master Address Table (24,064 Records): https://opendata.charlottesville.org/datasets/master-address-table
This table is intended to provide municipalities, residences, businesses, and application developers with a comprehensive set of standardized addresses for the City of Charlottesville.
- Special User Permit Area (186 Records): https://opendata.charlottesville.org/datasets/special-use-permit-area
A special use permit allows a landowner to obtain a tract of land for a use that does not fall directly under the permitted usage for that specifically zoned area. In most areas, the community is separated into different zones determined by the community’s zoning commission. These zones are then given a specific set of “by-right” permitted uses. This means that any land within that zone can be used for the permitted usage only, by right of the owner. In addition to the regular usages, under the local zoning regulations, each zone is usually given a “special uses” section allowing for uses that are just outside the intended uses for that zone. 
- Building Permits (26,961 Records): https://opendata.charlottesville.org/datasets/building-permits
This data set contains building permit information.  The City of Charlottesville requires a permit prior to the commencement of any construction, alteration, movement, enlargement, replacement, demolition or change the use or occupancy of a building or structure. The data is maintained daily and updates will display the next business day.

# Major Tasks
- PRE-PROCESSING, SAVE/READ CSV
   o Perform data pre-processing, data cleaning, outlier removal, etc to sanitize your data, if necessary
   o Save your data in a .csv file (or other format as appropriate for your data set and project scenario)
   o Read in data to your program from the .csv file
- DATAFRAME & CALCULATIONS
   o (Optional - do as appropriate) Process the data or perform any calculations or statistics on it before storing the data into a data frame (see next step)
   o Save the data into one or more data frame data structure (or other structure as appropriate) (review lecture notes/examples)
- QUERY
   o Once your data is stored query your data to reveal interesting/useful information based on your project scenario
   o Query your data using at least 4 different queries
   o Capture the results of the queries appropriately (either write results to a file, or store into another data structure, or do something else with the results as appropriate based on your project scenario)
- RESULTS
   o (Do as appropriate) Process the results, or submit additional queries to the obtained results (if results were saved to a file or another data structure)
   o Display final results in a presentable way (use tables and/or appropriate visualizations)
- TESTING
   o Perform adequate testing (TDD and/or Unit testing)
   o Submit this in a separate .py file
- POWERPOINT PRESENTATION
- WRITE-UP
   o INTRODUCTION: describe your project scenario. Starting out, what did you hope to accomplish/learn?
   o THE DATA: Describe your data set and its significance. Where did you obtain this data set from? Why did you choose the data set that you did? Indicate if you carried out any pre-processing/data cleaning/outlier removal, etc… to sanitize your data
   o BEYOND THE ORIGINAL SPECIFICATIONS: highlight clearly what things you did that went beyond the original specifications. That is, discuss what you implemented that would count towards the extra-credit portion of this project (see section below.)
   o RESULTS: Display and discuss the results. Describe what you have learned and mention the relevance/significance of the results you have obtained. Be sure to use appropriate visualizations to display your results.
   o TESTING: Describe what testing you did. Describe the Unit tests that you wrote. Show a sample run of one or two of your tests (screen caps or copy-and-paste is fine)
   o CONCLUSIONS: Summarize your findings, explain how these results could be used by others (if applicable), describe ways you could improve your program or ways you might like to expand the functionality of your program if given more time
