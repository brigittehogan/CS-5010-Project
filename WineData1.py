#!/usr/bin/env python
# coding: utf-8

# # Setting Up Data
# 
# Importing relevant libraries 
# 

# In[143]:


import pandas as pd
import matplotlib.pyplot as plt


# Setting up display so we can see all columns and rows

# In[144]:


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# Import the csv of 'red wine data' using ';' as the delimiter

# In[145]:


dfr = pd.read_csv('winequality-red.csv', sep=';')


# Viewing the first few rows of the data set
# 

# In[146]:


dfr.head()


# Getting a summary of each column in the data set

# In[147]:


dfr.describe()


# Finding the shape of the Data Frame

# In[148]:


dfr.shape



# Checking that each row has the correct Data Type

# In[149]:


dfr.dtypes


# # Data Preprocessing with Wine Query Class
# Create Wine Query Class with a DataFrame as the attribute

# In[177]:


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

## Count duplicates in the wine data

wineq1.count_dupes()

# Viewing Data for Outliers using Scatter Plots of Quality vs Attributes 

# In[152]:


fig, axes2 = plt.subplots(nrows=4, ncols=3, sharey= True)

dfr.plot(ax = axes2[0, 0], kind ='scatter', x = 'fixed acidity', y = 'quality', color = "red",
                title = 'quality vs '+ 'fixed acidity')
dfr.plot(ax = axes2[0, 1], kind ='scatter', x = 'volatile acidity', y = 'quality', color = "purple",
                title = 'quality vs '+ 'volatile acidity')
dfr.plot(ax = axes2[0, 2], kind ='scatter', x = 'citric acid', y = 'quality', color = "pink",
                title = 'quality vs '+ 'citric acid')
dfr.plot(ax = axes2[1, 0], kind ='scatter', x = 'residual sugar', y = 'quality', color = "green",
                title = 'quality vs '+ 'residual sugar')
dfr.plot(ax = axes2[1, 1], kind ='scatter', x = 'chlorides', y = 'quality', color = "blue",
                title = 'quality vs '+ 'chlorides')
dfr.plot(ax = axes2[1, 2], kind ='scatter', x = 'free sulfur dioxide', y = 'quality', color = "orange",
                title = 'quality vs '+ 'free sulfur dioxide')
dfr.plot(ax = axes2[2, 0], kind ='scatter', x = 'total sulfur dioxide', y = 'quality', color = "yellow",
                title = 'quality vs '+ 'total sulfur dioxide')
dfr.plot(ax = axes2[2, 1], kind ='scatter', x = 'density', y = 'quality', color = "violet",
                title = 'quality vs '+ 'density')
dfr.plot(ax = axes2[2, 2], kind ='scatter', x = 'pH', y = 'quality', color = "brown",
                title = 'quality vs '+ 'pH')
dfr.plot(ax = axes2[3, 0], kind ='scatter', x = 'sulphates', y = 'quality', color = "olive",
                title = 'quality vs '+ 'sulphates')
dfr.plot(ax = axes2[3, 1], kind ='scatter', x = 'alcohol', y = 'quality', color = "navy",
                title = 'quality vs '+ 'alcohol')
axes2[0, 0].set_ylabel('quality')
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=1.5)




# Check Volatile Acidity > 1.4

# In[153]:


wineq1.getrow('volatile acidity', 'greater than', 1.4)


# Check Chlorides > 0.6

# In[154]:


wineq1.getrow('chlorides', 'greater than', 0.6)


# Check Total Sulfur Dioxide > 250

# In[155]:


wineq1.getrow('total sulfur dioxide', 'greater than', 250)


# Check Sulphates greater than 1.75

# In[156]:


wineq1.getrow('sulphates', 'greater than', 1.75)


# # Sulphite Specific Queries
# How does the amount of Total Sulfur Dioxide (the amount that is added by the winemaker plus the amount naturally present in the wine) affect the quality rating of the wine?

# In[157]:


t_sulf_means = wineq1.getmeans_for_att('total sulfur dioxide')
type(t_sulf_means)
print(t_sulf_means)
t_sulf_means.plot(kind = "bar", title = "Mean Total Sulfur Dioxide by Quality Rating", color = "purple",
                  x = "quality", y = "mean total sulfur dioxide")


# How does the amount of Free Sulfur Dioxide (the amount added by the winemaker) affect the quality rating of the wine?

# In[158]:


f_sulf_means = wineq1.getmeans_for_att('free sulfur dioxide')
f_sulf_means.plot(kind = "bar", title = "Mean Free Sulfur Dioxide by Quality Rating", color = "green",
                  x = "quality", y = "mean free sulfur dioxide")
                 


# How does the mean bound sulfur relate to these patterns?  The bound sulfur is Total - Free.

# In[159]:


dfwb = wineq1.new_bound_sulfites()  ## name new data frame with bound sulfites as an additional column

b_sulf_means = wineq1.getmeans_for_att('bound sulfur dioxide')
b_sulf_means.plot(kind = "bar", title = "Mean Bound Sulfur Dioxide by Quality Rating", color = "aqua",
                  x = "quality", y = "mean bound sulfur dioxide")



# Finding the wines where 'total sulfur dioxide' > 160

# In[162]:


wineq1.getrow("total sulfur dioxide", "greater than", 160)


# Finding the wines were 'total sulfur dioxide' < 10

# In[169]:


wineq1.getrow("total sulfur dioxide", "less than", 10)


# Counting the wines that have 'total sulfur dioxide' < 10

# In[163]:


wineq1.getrow("total sulfur dioxide", "less than", 10).count()



###Printing all three graphs in same plot, side-by-side

fig, axes = plt.subplots(nrows=1, ncols=3, sharey= True)
t_sulf_means.plot(ax=axes[0], kind = "bar", title = "Sulfur Dioxide by Quality", color = "purple",
                  x = "quality", y = "mean total sulfur dioxide")
f_sulf_means.plot(ax=axes[1], kind = "bar", title = "Sulfur Dioxide by Quality", color = "green",
                  x = "quality", y = "mean free sulfur dioxide")
b_sulf_means.plot(ax=axes[2], kind = "bar", title = "Sulfur Dioxide by Quality", color = "aqua",
                  x = "quality", y = "mean bound sulfur dioxide")
axes[0].set_ylabel('Sulfur Dioxide (ppm)')



# Summary statistics for the reduced data frame where 'total sulfur' < 10.  Data frame named 'dfx'.

# In[170]:


print("================================================================")





dfx = (wineq1.getrow("total sulfur dioxide", "less than", 10))
wineq3 = WineQuery(dfx)
dfx.describe()


# Rewriting summary statistics for entire data set for comparison

# In[171]:


dfr.describe()
type(dfr.describe())

# In[173]:

# Plotting the mean values for each column for the original and low SO2 data frames

fig, axes = plt.subplots(nrows=1, ncols=2, sharey= True)
dfr.describe().loc['mean'].plot(ax=axes[0], kind = "bar", color = 'blue', title = 'Original SO2 Data', y = 'values')
dfx.describe().loc['mean'].plot(ax=axes[1], kind = 'bar', color = 'green', title = 'Lower SO2 Data', y = 'values')
axes[0].set_ylabel('Variable Means')







