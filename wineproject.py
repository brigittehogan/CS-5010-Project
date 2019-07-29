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

