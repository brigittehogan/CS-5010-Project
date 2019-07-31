import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

#setting display so we can see all columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#import the csv of red wine data using ';' as delimiter
dfr = pd.read_csv('winequality-red.csv', ',')
summary =dfr.describe()

class Alcohol:
   def  __init__(self):
       self = self
       
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
        
   def alcohol_low(dataframe): #filtering out low alcohol content wines and putting them into a dataframe, using the percentile functions above
        pd.a_filtered = dataframe[(dataframe.alcohol < Alcohol.low_extremes(dataframe, 'alcohol'))]
        return pd.a_filtered
    
   def alcohol_high(dataframe): #filtering out high alcohol content wines and putting them into a dataframe, using the percentile functions above
        pd.a_filtered = dataframe[(dataframe.alcohol > Alcohol.high_extremes(dataframe, 'alcohol'))]
        return pd.a_filtered
    
   def alcohol_hohum(dataframe): #using the low_extremes and high_extremes functions to filter out only those in the middle, and putting them into a dataframe 
        pd.a_filtered = dataframe[(dataframe.alcohol >= Alcohol.low_extremes(dataframe, 'alcohol')) & (dataframe.alcohol <= Alcohol.high_extremes(dataframe, 'alcohol'))]
        return pd.a_filtered
    
    #analysis functions
    
   def low_quality(dataframe,quality): #creating a function that allows you to filter the low alcohol content wines by quality
        pd.a_filtered = dataframe[(dataframe.alcohol < Alcohol.low_extremes(dataframe, 'alcohol')) & (dataframe.quality > quality)]
        return pd.a_filtered
    
   def high_quality(dataframe, quality): #creating a function that allows you to filter the high  alcohol content wines by quality
        pd.a_filtered = dataframe[(dataframe.alcohol > Alcohol.high_extremes(dataframe, 'alcohol')) & (dataframe.quality > quality)]
        return pd.a_filtered
    
   def alcohol_hohum2(dataframe, quality): #creating a function that allows you to filter the normal  alcohol content wines by quality
        pd.a_filtered = dataframe[(dataframe.alcohol >= Alcohol.low_extremes(dataframe, 'alcohol')) & (dataframe.alcohol <= Alcohol.high_extremes(dataframe, 'alcohol')) & (dataframe.quality > quality)]
        return pd.a_filtered
    
    
#Analysis Code

#putting all of the alcohol subgroup dataframes into objects, using the functions above
alc_low = Alcohol.alcohol_low(dfr)
alc_high = Alcohol.alcohol_high(dfr)
alc_norm = Alcohol.alcohol_hohum(dfr)

#taking the means of these subgroups
low_mean = alc_low.quality.mean()
high_mean = alc_high.quality.mean()
middle_mean = alc_norm.quality.mean()

#taking the standard deviations of these subgroups
alc_low.quality.std()
alc_high.quality.std()
alc_norm.quality.std()

#testing out how many wines from each subgroup are above 6
above6low = Alcohol.low_quality(dfr, 6)
above6high = Alcohol.high_quality(dfr, 6)
above6norm = Alcohol.alcohol_hohum2(dfr, 6)

#first chart
x_axis = ('Bottom 5%', 'Middle 90%', 'Top 5%')
means = [low_mean, middle_mean, high_mean]
y_pos = np.arange(len(means))
help(plt.bar)
plt.bar(y_pos, means, align='center', alpha=0.5, color='blue' )
plt.xticks(y_pos, x_axis)
plt.ylabel('Mean Quality')
plt.title('Mean Quality by Alcohol Content')
plt.show()

#2nd chart
num_bins = 100
n, bins, patches = plt.hist(dfr.alcohol, num_bins, facecolor='blue', alpha=0.5)
plt.ylabel('# of Wines')
plt.xlabel('% Alcohol Content')
plt.title('Histogram of Wines by Alcohol Content')

plt.show()









    
        