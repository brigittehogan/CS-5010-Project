# -*- coding: utf-8 -*-
"""
#Sherry Kausch
#query 2 of CS 5010 Final Project
"""
#importing necessary libraries
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#setting display so we can see all columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#reading in the dataset from the csv file
dfr = pd.read_csv('winequality-red.csv', sep=';')

##################################################################################

#preprossing with respect to acidity query
#renaming varaibale to get rid of spaces
dfr = dfr.rename(columns = {"fixed acidity": "fixed_acidity", 
                                  "volatile acidity":"volatile_acidity",
                                  "residual sugar":"residual_sugar"}) 

#creating new variable 'total_acidity' that is the sum of fixed and volitile acidity
dfr['total_acidity'] = dfr['fixed_acidity'] + dfr['volatile_acidity']

#finding the minimum and maximum acidity levels 
dfr['total_acidity'].max()
dfr['total_acidity'].min()

#finding the minimum and maximum pH levels 
dfr['pH'].max()
dfr['pH'].min()

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

#creating bins for total acidity
#assigning total acidity lower than typically found in wines to "low" and those that 
#are higher than typical to "high" all else to "typical"
dfr['Acid_level'] = pd.cut(x=dfr['total_acidity'], bins=[0, 4, 9, 17], labels=['low', 'typical', 'high'])
dfr['Acid_level'].describe
dfr['Acid_level'].value_counts()


class WineAcidQuery():

    def __init__(self, df, var1, var2): ## creates the class by taking in a data frame as the attribute
        self.df = df 
        self.var1 = var1
        self.var2 = var2
        
#creating method for getting the mean of all variables after grouping by two variables
    def groupMeans(self):
        return self.df.groupby([self.var1, self.var2]).mean()

#creating method for getting the mean of all variables after grouping by two variables
    def groupSize(self):
        return self.df.groupby([self.var1, self.var2]).size()

#creating method for getting the mean of all variables after grouping by two variables
    def groupDescribe(self):
        return self.df.groupby([self.var1, self.var2]).describe()
    

wine1 = WineAcidQuery(dfr, 'quality', 'Acid_level')
#using my methods to get means, group sizes, and description of all wine chemestry variables by quality and acid level
wine1.groupMeans()
wine1.groupSize()
wine1.groupDescribe()

############################################################################
#creating nested bar plot to show acid level county by quality rating
n_groups = 6
typical_count = (5, 38, 445, 400, 94, 9)
high_count = (5, 15, 236, 238, 105, 9)


fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rectsl = plt.bar(index, typical_count, bar_width)
alpha=opacity,
color='b'
labes = 'Typical Acidity'
rects2 = plt.bar(index + bar_width, high_count, bar_width,
                 alpha = opacity, color = 'g', label = 'High Acidity')
labes = 'High Acidity'
plt.xlabel('Quality')
plt.ylabel('Counts')
plt.title('Counts of High and Typical Acid Wine by Quality')
plt.xticks(index + bar_width, ('3', '4', '5', '6', '7', '8'))
plt.legend()

plt.tight_layout()
plt.show()

#creating nested bar plot to show mean residual sugar level by acid level and quality rating
n_groups = 6
typical_meansug = (3.010000, 2.821053, 2.430787, 2.359750, 2.486702, 2.122222)
high_meansug = (2.260000, 2.373333, 2.713771, 2.674580 , 2.930000, 3.033333)

fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rectsl = plt.bar(index, typical_meansug, bar_width)
alpha=opacity,
color='b'
labes = 'Typical Acidity'
rects2 = plt.bar(index + bar_width, high_meansug, bar_width,
                 alpha = opacity, color = 'g', label = 'High Acidity')
labes = 'High Acidity'
plt.xlabel('Quality')
plt.ylabel('Mean Residual Sugar Level')
plt.title('Residual Sugar of High and Typical Acid Wine by Quality')
plt.xticks(index + bar_width, ('3', '4', '5', '6', '7', '8'))
plt.legend()
plt.tight_layout()
plt.show()

#########################################################################
