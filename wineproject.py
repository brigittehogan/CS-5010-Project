#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#### Reading the csv's into python and running some preliminary plots

import csv
import pandas as pd
import matplotlib.pyplot as plt

from ResidualSugar import * # reading in ResidualSugar class
from WineQuery import *     # reading in WineQuery class

#setting display so we can see all columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


#import the csv of red wine data using ';' as delimiter
dfr = pd.read_csv('winequality-red.csv', sep=';')

#viewing the first few rows of the data set
dfr.head()

#getting a summary of each column in the data set
dfr.describe()

# scatter plots of y = quality vs each column
dfr.shape

# Checking that each row has the correct Data Type
dfr.dtypes

# # Data Preprocessing with Wine Query Class
# Create Wine Query Class with a DataFrame as the attribute
# ============================================================================================
class WineQuery():

    def __init__(self, df): ## creates the class by taking in a data frame as the attribute
        self.df = df  
            
    def count_nulls(self):## counts how many nulls are in each column
        if self.df.empty == True :
            return print("This data frame is entirely empty")
        else:
            return self.df.isnull().sum()
       
    def getmeans_for_att(self, attribute): ## takes in an attribute, groups the data 
        #frame by that quality, and returns the means of that attribute by quality rating
        grouped = self.df.groupby(['quality'])[attribute].mean().reset_index(name=
                                 'mean ' + attribute)
        return grouped
    
    def getmeans_for_q_rating(self, attribute, rating): ## takes in a quality rating, groups the data 
        #frame by that rating, and returns the means of the other attributes for that quality rating
        grouped = self.df.groupby(['quality'])[attribute].mean()
        return grouped.iloc[rating-3]
    
    def q_scatter_plot(self, attribute, color = 'blue'): ##takes in an attribute and prints a scatter plot of the quality
        #rating vs that attribute
        dfr.plot(kind ='scatter', x = attribute, y = 'quality', color = color,
                title = 'quality vs '+ attribute)
        return plt.show()
    
    def getrow(self, attribute, command, number): ## takes in an attribute and a boolean function, and returns the row
        #of samples for which the boolean function is true
        if command == "greater than":
            return self.df[self.df[attribute] > number] 
        elif command == "less than":
            return self.df[self.df[attribute] < number]
        elif command == "equal to":
            return self.df[self.df[attribute] == number]
        else:
            print('Please choose "greater than", "less than" or "equal to"')
         
    def count_dupes(self):
        return self.df.duplicated().sum()
    
    def new_bound_sulfites(self):
        self.df['bound sulfur dioxide'] = self.df['total sulfur dioxide'] - self.df['free sulfur dioxide']
        return self.df['bound sulfur dioxide']
    
# Initialize wine1 as a member of the WineQuery class

wineq1 = WineQuery(dfr)

# Viewing Data for Outliers using Scatter Plots of Quality vs Attributes 

wineq1.q_scatter_plot('fixed acidity', "red")
wineq1.q_scatter_plot('volatile acidity', "blue")
wineq1.q_scatter_plot('citric acid', "green")
wineq1.q_scatter_plot('residual sugar', "brown")
wineq1.q_scatter_plot('chlorides', "orange")
wineq1.q_scatter_plot('free sulfur dioxide', "purple")
wineq1.q_scatter_plot('total sulfur dioxide', "pink")
wineq1.q_scatter_plot('density', "olive")
wineq1.q_scatter_plot('pH', "navy")
wineq1.q_scatter_plot('sulphates', "yellow")
wineq1.q_scatter_plot('alcohol', "violet")

# Check Volatile Acidity > 1.4
wineq1.getrow('volatile acidity', 'greater than', 1.4)

# Check Chlorides > 0.6
wineq1.getrow('chlorides', 'greater than', 0.6)

# Check Total Sulfur Dioxide > 250
wineq1.getrow('total sulfur dioxide', 'greater than', 250)

# Check Sulphates greater than 1.75
wineq1.getrow('sulphates', 'greater than', 1.75)

# ============================================================================================
# # Sulphite Specific Queries
# How does the amount of Total Sulfur Dioxide (the amount that is added by the winemaker 
#plus the amount naturally present in the wine) affect the quality rating of the wine?

f_sulf_means = wineq1.getmeans_for_att('total sulfur dioxide')
type(f_sulf_means)
print(f_sulf_means)
f_sulf_means.plot(kind = "bar", title = "Mean Total Sulfur Dioxide by Quality Rating", color = "purple",
                  x = "quality", y = "mean total sulfur dioxide")


# How does the amount of Free Sulfur Dioxide (the amount added by the winemaker) affect the quality rating of the wine?

f_sulf_means = wineq1.getmeans_for_att('free sulfur dioxide')
f_sulf_means.plot(kind = "bar", title = "Mean Free Sulfur Dioxide by Quality Rating", color = "green",
                  x = "quality", y = "mean free sulfur dioxide")
                 
# How does the mean bound sulfur relate to these patterns?  The bound sulfur is Total - Free.

dfwb = wineq1.new_bound_sulfites()  ## name new data frame with bound sulfites as an additional column

b_sulf_means = wineq1.getmeans_for_att('bound sulfur dioxide')
b_sulf_means.plot(kind = "bar", title = "Mean Bound Sulfur Dioxide by Quality Rating", color = "aqua",
                  x = "quality", y = "mean bound sulfur dioxide")

# Finding the wines where 'total sulfur dioxide' > 160
wineq1.getrow("total sulfur dioxide", "greater than", 160)


# Finding the wines were 'total sulfur dioxide' < 10
wineq1.getrow("total sulfur dioxide", "less than", 10)


# Counting the wines that have 'total sulfur dioxide' < 10
wineq1.getrow("total sulfur dioxide", "less than", 10).count()


# Summary statistics for the reduced data frame where 'total sulfur' < 10.  Data frame named 'dfx'.

dfx = (wineq1.getrow("total sulfur dioxide", "less than", 10))
wineq3 = WineQuery(dfx)
dfx.describe()


# Rewriting summary statistics for entire data set for comparison
dfr.describe()
type(dfr.describe())

# Plotting the mean values for each column for the original and low SO2 data frames
dfr.describe().loc['mean'].plot(kind = "bar", color = 'blue', title = 'Original(blue) and Lower SO2 (yellow) Data')
dfx.describe().loc['mean'].plot(kind = 'bar', color = 'yellow')

#################################################################################
print('=====================================================================')



#percentile functions

def high_extremes(dataframe, column): # finding the 95th percentile of a column of the data
    dfcolumn = dataframe[column]
    highq = dfcolumn.quantile(q = .95)
    return highq
def low_extremes(dataframe, column): #finding the 5th percentile of a column of the data
    dfcolumn = dataframe[column]
    lowq = dfcolumn.quantile(q = .05)
    return lowq

#subgrouping functions
    
def alcohol_low(): #filtering out low alcohol content wines and putting them into a dataframe, using the percentile functions above
    pd.a_filtered = dfr[(dfr.alcohol < low_extremes(dfr, 'alcohol'))]
    return pd.a_filtered

def alcohol_high(): #filtering out high alcohol content wines and putting them into a dataframe, using the percentile functions above
    pd.a_filtered = dfr[(dfr.alcohol > high_extremes(dfr, 'alcohol'))]
    return pd.a_filtered

def alcohol_hohum(): #using the low_extremes and high_extremes functions to filter out only those in the middle, and putting them into a dataframe 
    pd.a_filtered = dfr[(dfr.alcohol >= low_extremes(dfr, 'alcohol')) & (dfr.alcohol <= high_extremes(dfr, 'alcohol'))]
    return pd.a_filtered

#analysis functions

def low_quality(quality): #creating a function that allows you to filter the low alcohol content wines by quality
    pd.a_filtered = dfr[(dfr.alcohol < low_extremes(dfr, 'alcohol')) & (dfr.quality > quality)]
    return pd.a_filtered

def high_quality(quality): #creating a function that allows you to filter the high  alcohol content wines by quality
    pd.a_filtered = dfr[(dfr.alcohol > high_extremes(dfr, 'alcohol')) & (dfr.quality > quality)]
    return pd.a_filtered

def alcohol_hohum2(quality): #creating a function that allows you to filter the normal  alcohol content wines by quality
    pd.a_filtered = dfr[(dfr.alcohol >= low_extremes(dfr, 'alcohol')) & (dfr.alcohol <= high_extremes(dfr, 'alcohol')) & (dfr.quality > quality)]
    return pd.a_filtered

#function to count the numebr of rows
def countrows(dataframe):
    return dataframe.count()
    
#Analysis Code

#putting all of the alcohol subgroup dataframes into objects, using the functions above
alc_low = alcohol_low()
alc_high = alcohol_high()
alc_norm = alcohol_hohum()

#taking the means of these subgroups
alc_low.quality.mean()
alc_high.quality.mean()
alc_norm.quality.mean()

#taking the standard deviations of these subgroups
alc_low.quality.std()
alc_high.quality.std()
alc_norm.quality.std()

#testing out how many wines from each subgroup are above 6
above6low = low_quality(6)
above6high = high_quality(6)
above6norm = alcohol_hohum2(6)
countrows(above6high)
countrows(above6norm)
countrows(above6low)

# ============================================================================================
## Residual Sugar analysis

# Viewing Data for Outliers using Scatter Plots
dfr.plot(kind ='scatter', x = 'residual sugar', y = 'quality', color = 'brown',
                title = '')

# check Residual Sugar > 12
wineq1 = WineQuery(dfr) # Initialize wine1 as a member of the WineQuery class
wineq1.getrow('residual sugar', 'greater than', 12)

# Querying Data Set ----------------------------------------------------------
# initialize temp as member of ResidualSugar class
# Note: assigning to temp also makes changes to dfr
temp = ResidualSugar(dfr, 'residual sugar') 

temp.convert_to_gdm3()
temp.convert_to_gmL()
temp.convert_to_gserve()

# classify wine sweetness
temp.classify_sugar(scheme='US')
temp.classify_sugar(scheme='EU')

# summary stats
dfr.head()
dfr.loc[dfr['residual sugar'] < 1]
len(dfr.loc[dfr['residual sugar']>10])/1599 * 100 #
len(dfr.loc[dfr['residual sugar']<10])/1599 * 100 # 99.3%

dfr['rs_type_US'].describe()
dfr['rs_type_EU'].describe()


quality_group = dfr.groupby(['quality'])
quality_group['residual sugar'].describe()

US_type_group = dfr.groupby(['rs_type_US'])
US_type_group['residual sugar'].describe()

EU_type_group = dfr.groupby(['rs_type_EU'])
EU_type_group['residual sugar'].describe()

# Summary Plots -------------------------------------------------------------

#histogram of the residual level
dfr['residual sugar'].plot.hist(grid=False, bins=20, rwidth=0.9,
                   color='brown', figsize=(6,4))
plt.title('Histogram of Residual Sugar in Vinho Verde Wines')
plt.xlabel('Residual Sugar (g/dm3)')
plt.ylabel('Number of Samples')
plt.grid(axis='y', alpha=0.75)  

# BoxPlots - attribute on y
temp.boxplot_quality('residual sugar', ylabel="residual sugar (g/dm3)")

# BoxPlot - quality on y
bins   = [0, 5, 10, 15, 20]
labels = ['0 - 4.9', '5.0 - 9.9', '10.0 - 14.5', '15.0+']
temp.boxplot_attrBin('residual sugar', bins, labels)

# View by group
sugar_group = dfr.groupby(['residual sugarBin'])
sugar_group['residual sugar'].describe()

#scatterplot of residual sugar and pH, with quality as the color of the dots
marker_size=15
plt.scatter(dfr['residual sugar'], dfr['pH'], c = dfr['quality'])
cbar = plt.colorbar()
cbar.set_label("Quality Rating")
plt.title('')
plt.xlabel('residual sugar')
plt.ylabel('pH')
plt.show()


print('============================================================================================================')

## Acidity analysis

#preprossing with respect to acidity query  -------------------------------------------------------------
#renaming varaibale to get rid of spaces
dfr = dfr.rename(columns = {"fixed acidity": "fixed_acidity", 
                                  "volatile acidity":"volatile_acidity"}) 

#creating new variable 'total_acidity' that is the sum of fixed and volitile acidity
dfr['total_acidity'] = dfr['fixed_acidity'] + dfr['volatile_acidity']

#creating bins for total acidity
#assigning total acidity lower than typically found in wines to "low" and those that 
#are higher than typical to "high" all else to "typical"
dfr['Acid_level'] = pd.cut(x=dfr['total_acidity'], bins=[0, 4, 8, 100], labels=['low', 'typical', 'high'])

#finding the minimum and maximum acidity levels 
dfr['total_acidity'].max()
dfr['total_acidity'].min()

#finding the minimum and maximum pH levels 
dfr['pH'].max()
dfr['pH'].min()

# Summary Plots -------------------------------------------------------------
#histogram of the total acidity level
dfr['total_acidity'].plot.hist(grid=True, bins=20, rwidth=0.9,
                   color='#607c8e')
plt.title('Total Acidity Level')
plt.xlabel('Total Acidity')
plt.ylabel('Counts')
plt.grid(axis='y', alpha=0.75)    
                            
#histogram of the pH level
dfr['pH'].plot.hist(grid=True, bins=20, rwidth=0.9,
                   color='#607c8e')
plt.title('Wine pH Level')
plt.xlabel('pH')
plt.ylabel('Counts')
plt.grid(axis='y', alpha=0.75)

#scatterplot of total acidity and pH, with quality as the color of the dots
marker_size=15
plt.scatter(dfr['total_acidity'], dfr['pH'], c = dfr['quality'])
cbar = plt.colorbar()
cbar.set_label("Quality Rating")
plt.title('Scatter plot of the total acidity and pH of wine')
plt.xlabel('Total Acidity')
plt.ylabel('pH')
plt.show()

# Create Wine Acid Query Class with a DataFrame and two variables as the attributes
# ============================================================================================

class WineAcidQuery():

    def __init__(self, df, var1, var2): ## creates the class by taking in a data frame as the attribute
        self.df = df 
        self.var1 = var1
        self.var2 = var2
        
#creating method for getting the mean of all variables after grouping by two variables
    def groupMeans(self, var1, var2):
        return self.df.groupby([var1, var2]).mean()

#creating method for getting the mean of all variables after grouping by two variables
    def groupSize(self, var1, var2):
        return self.df.groupby([var1, var2]).size()

#creating method for getting the mean of all variables after grouping by two variables
    def groupDescribe(self, var1, var2):
        return self.df.groupby([var1, var2]).describe()
 
# ============================================================================================
# # Acid Specific Queries
    
wine1 = WineAcidQuery(dfr, 'quality', 'Acid_level')
#using my methods to get means, group sizes, and description of all wine chemestry variables by quality and acid level
wine1.groupMeans('quality', 'Acid_level')
wine1.groupSize('quality', 'Acid_level')
wine1.groupDescribe('quality', 'Acid_level')

print('============================================================================================================')

#Conducting Unit Testing on the Classes:

#import unittest module
import unittest

#testing WineQuery Class
class WineQueryTests(unittest.TestCase): # inherit from unittest.TestCase
   
    #test winequery init for all df cases, and what happens frame is empty
    def test_WineQuery_init_reg_df(self): #testing the init method with a regular data frame with string and
        #integer values
        wineq1 = WineQuery(df1)        
        #Test that data frame can be extracted
        assert_frame_equal(wineq1.df, df1)
             
    def test_WineQuery_init_zero_na_df(self): #testing the init method with a regular data frame with values
        wineq2 = WineQuery(df2)        
        #Test that data frame can be extracted
        assert_frame_equal(wineq2.df, df2)
    
    def test_WineQuery_init_float_df(self): #testing the init method with a regular data frame with float values
        wineq3 = WineQuery(df3)        
        #Test that data frame can be extracted
        assert_frame_equal(wineq3.df, df3)  
               
    def test_count_nulls_some(self): #testing that this method counts nulls correctly
        #use df2 data frame with null value
        wineq2 = WineQuery(df2)
        pd.testing.assert_series_equal(wineq2.count_nulls(), wineq2.df.isnull().sum())
        
    def test_count_nulls_all(self): #testing that this method counts nulls correctly
        #when given an empty data frame
        df4 = pd.DataFrame()
        wineq4 = WineQuery(df4)
        self.assertEqual(wineq4.count_nulls(), print ("This data frame is entirely empty"))
      
    def test_getmeans_for_att(self): ## test to see that the function renders the correct 
        # data frame result when the attribute is density
        wineq5 = WineQuery(dfr)
        dft = wineq5.getmeans_for_att('density')
        assert_frame_equal(dft, dfr.groupby(['quality'])['density'].mean().reset_index(name=
                                 'mean ' + 'density'))
    
    def test_getrow_greater_than(self): #test getrow with "greater than"
        wineq5 = WineQuery(dfr)
        assert_frame_equal(wineq5.getrow("density", "greater than", 0.9), dfr[dfr["density"] > 0.9])
        
    def test_getrow_less_than(self): #test getrow with "less than"
        wineq5 = WineQuery(dfr)
        assert_frame_equal(wineq5.getrow("density", "less than", 0.2), dfr[dfr["density"] < 0.2])
        
    def test_getrow_equal_to(self): #test getrow with "equal to"
        wineq5 = WineQuery(dfr)
        assert_frame_equal(wineq5.getrow("density", "equal to", 0.2), dfr[dfr["density"] == 0.2])
        
    def test_getrow_wrong_command(self): #test getrow with wrong command
        wineq5 = WineQuery(dfr)
        self.assertEqual(wineq5.getrow("density", "about", 5), 
                         print('Please choose "greater than", "less than" or "equal to"'))
    
    def test_count_dupes_2(self): #test that duplicate rows are counted correctly when there are dupes
        data1 = {'Color':['Yellow', 'Red', 'Blue', 'Green', 'Yellow', 'Red'], 'Count':[1, 2, 3, 4, 1, 2]} 
        df1 = pd.DataFrame(data1) 
        wineq1 = WineQuery(df1)
        self.assertEqual(wineq1.count_dupes(), 2)
    
    def test_count_dupes_0(self): #test that duplicate rows are counted correctly when there are no dupes
        data2 = {'Color':['Yellow', 'na', 'Blue', 'Green'], 'Count':[1, 2, 0, 4]} 
        df2 = pd.DataFrame(data2)  
        wineq2 = WineQuery(df2)
        self.assertEqual(wineq2.count_dupes(), 0)
        
    def test_new_bound_sulfites(self): #test that the data frame subtraction worked correctly
        #by extracting the first terms of the two columns in the original dataframe and confirm
        #that the correct difference was calculated and put into the right column
        wineq5 = WineQuery(dfr)
        dfx = wineq5.new_bound_sulfites()
        self.assertEqual(dfx[0], (wineq5.df.loc[0, 'total sulfur dioxide'] - wineq5.df.loc[0, 'free sulfur dioxide']))
                   
        
        
        
if __name__ == '__main__':
    unittest.main() 
