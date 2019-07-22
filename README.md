# CS-5010-Project
Wine!

## Links
* UCI Machine Learning Datasets: https://archive.ics.uci.edu/ml/datasets.php
* Wine Quality: https://archive.ics.uci.edu/ml/datasets/Wine+Quality
  * Data Folder: https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/
  * Data Description

## Data
* Wine Quality (4,898 Records):<p>
The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine. For more details, consult: [Web Link] or the reference [Cortez et al., 2009]. Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).

These datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are many more normal wines than excellent or poor ones). Outlier detection algorithms could be used to detect the few excellent or poor wines. Also, we are not sure if all input variables are relevant. So it could be interesting to test feature selection methods.</p>

* Attribute Informaion (12 Attributes):
  * Input variables (based on physicochemical tests): 
     1 - fixed acidity 
     2 - volatile acidity 
     3 - citric acid 
     4 - residual sugar 
     5 - chlorides 
     6 - free sulfur dioxide 
     7 - total sulfur dioxide 
     8 - density 
     9 - pH 
     10 - sulphates 
     11 - alcohol 
   * Output variable (based on sensory data): 
     12 - quality (score between 0 and 10)
     
* Files
  * winequality-red.csv - red wine preference samples
  * winequality-white.csv - white wine preference samples
  
* References
   * Source: Paulo Cortez, University of Minho, Guimarães, Portugal, http://www3.dsi.uminho.pt/pcortez 
   * A. Cerdeira, F. Almeida, T. Matos and J. Reis, Viticulture Commission of the Vinho Verde Region(CVRVV), Porto, Portugal 
    @2009
   * Paper: P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009. https://www.sciencedirect.com/science/article/pii/S0167923609001377?via%3Dihub
   * Details on vino verde http://www.vinhoverde.pt/en/

## Major Tasks
* PRE-PROCESSING, SAVE/READ CSV
  * Perform data pre-processing, data cleaning, outlier removal, etc to sanitize your data, if necessary
  * Save your data in a .csv file (or other format as appropriate for your data set and project scenario)
  * Read in data to your program from the .csv file
* DATAFRAME & CALCULATIONS
  * (Optional - do as appropriate) Process the data or perform any calculations or statistics on it before storing the data into a data frame (see next step)
  * Save the data into one or more data frame data structure (or other structure as appropriate) (review lecture notes/examples)
* QUERY
  * Once your data is stored query your data to reveal interesting/useful information based on your project scenario
  * Query your data using at least 4 different queries
  * Capture the results of the queries appropriately (either write results to a file, or store into another data structure, or do something else with the results as appropriate based on your project scenario)
* RESULTS
  * (Do as appropriate) Process the results, or submit additional queries to the obtained results (if results were saved to a file or another data structure)
  * Display final results in a presentable way (use tables and/or appropriate visualizations)
* TESTING
  * Perform adequate testing (TDD and/or Unit testing)
  * Submit this in a separate .py file
* CODE CONSOLIDATION
  * Ensure code works smoothly
  * Ensure code is properly commented
* POWERPOINT PRESENTATION
* WRITE-UP

### Write-up Details
* INTRODUCTION:
  * describe your project scenario
  * Starting out, what did you hope to accomplish/learn?
* THE DATA: 
  * Describe your data set and its significance. 
  * Where did you obtain this data set from? 
  * Why did you choose the data set that you did? 
  * Indicate if you carried out any pre-processing/data cleaning/outlier removal, etc… to sanitize your data
* BEYOND THE ORIGINAL SPECIFICATIONS:
  * Highlight clearly what things you did that went beyond the original specifications. That is, discuss what you implemented that would count towards the extra-credit portion of this project (see section below.)
* RESULTS: 
  * Display and discuss the results. 
  * Describe what you have learned and mention the relevance/significance of the results you have obtained. 
  * Be sure to use appropriate visualizations to display your results.
* TESTING: 
  * Describe what testing you did. 
  * Describe the Unit tests that you wrote. 
  * Show a sample run of one or two of your tests (screen caps or copy-and-paste is fine)
* CONCLUSIONS: 
  * Summarize your findings, explain how these results could be used by others (if applicable), describe ways you could improve your program or ways you might like to expand the functionality of your program if given more time
