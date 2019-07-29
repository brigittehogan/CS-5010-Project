#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#### Reading the csv's into python and running some preliminary plots

import csv
import pandas as pd
import matplotlib.pyplot as plt


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

#############################################################################
print('====================================================================')

# first run ResidualSugar.py
temp = ResidualSugar(dfr, 'residual sugar') # assigning to temp also makes changes to dfr
temp.convert_to_gdm3()
temp.convert_to_goz()
temp.convert_to_gserve()
temp.classify_sugar()

# view results
dfr.head()
dfr.loc[dfr['residual sugar'] < 1]

