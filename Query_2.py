# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 19:27:53 2019

@author: Student
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 14:40:36 2019

@author: Student
"""

import csv
import pandas as pd
import matplotlib.pyplot as plt


#setting display so we can see all columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

dfr = pd.read_csv('winequality-red.csv', sep=';')

##################################################################################

#preprossing with respect to acidity query
#renaming varaibale to get rid of spaces
dfr = dfr.rename(columns = {"fixed acidity": "fixed_acidity", 
                                  "volatile acidity":"volatile_acidity"}) 

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
dfr['Acid_level'] = pd.cut(x=dfr['total_acidity'], bins=[0, 4, 8, 100], labels=['low', 'typical', 'high'])


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
 

    
wine1 = WineAcidQuery(dfr, 'quality', 'Acid_level')
#using my methods to get means, group sizes, and description of all wine chemestry variables by quality and acid level
wine1.groupMeans('quality', 'Acid_level')
wine1.groupSize('quality', 'Acid_level')
wine1.groupDescribe('quality', 'Acid_level')
