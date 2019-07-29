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
dfr.plot(kind='scatter',x='fixed acidity',y='quality',color='purple')
plt.show()

dfr.plot(kind='scatter',x='volatile acidity',y='quality',color='green')
plt.show()

dfr.plot(kind='scatter',x='citric acid',y='quality',color='yellow')
plt.show()

dfr.plot(kind='scatter',x='residual sugar',y='quality',color='blue')
plt.show()

dfr.plot(kind='scatter',x='chlorides',y='quality',color='lightseagreen')
plt.show()

dfr.plot(kind='scatter',x='free sulfur dioxide',y='quality',color='darkolivegreen')
plt.show()

dfr.plot(kind='scatter',x='total sulfur dioxide',y='quality',color='lightcoral')
plt.show()

dfr.plot(kind='scatter',x='density',y='quality',color='skyblue')
plt.show()

dfr.plot(kind='scatter',x='pH',y='quality',color='orangered')
plt.show()

dfr.plot(kind='scatter',x='sulphates',y='quality',color='sienna')
plt.show()

dfr.plot(kind='scatter',x='alcohol',y='quality',color='darkblue')
plt.show()

#############################################################################
print('====================================================================')

#read csv of white wine dataset using ';' as delimiter
dfw = pd.read_csv('winequality-white.csv', sep=';')

#view first few rows of white wine data set
dfw.head()

#view summaries of each column in the white wine data set
dfw.describe()

# scatterplots with y = 'quality' vs each column individually
dfw.plot(kind='scatter',x='fixed acidity',y='quality',color='purple')
plt.show()

dfw.plot(kind='scatter',x='volatile acidity',y='quality',color='green')
plt.show()

dfw.plot(kind='scatter',x='citric acid',y='quality',color='yellow')
plt.show()

dfw.plot(kind='scatter',x='residual sugar',y='quality',color='blue')
plt.show()

dfw.plot(kind='scatter',x='chlorides',y='quality',color='lightseagreen')
plt.show()

dfw.plot(kind='scatter',x='free sulfur dioxide',y='quality',color='darkolivegreen')
plt.show()

dfw.plot(kind='scatter',x='total sulfur dioxide',y='quality',color='lightcoral')
plt.show()

dfw.plot(kind='scatter',x='density',y='quality',color='skyblue')
plt.show()

dfw.plot(kind='scatter',x='pH',y='quality',color='orangered')
plt.show()

dfw.plot(kind='scatter',x='sulphates',y='quality',color='sienna')
plt.show()

dfw.plot(kind='scatter',x='alcohol',y='quality',color='darkblue')
plt.show()

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

