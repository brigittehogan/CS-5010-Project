#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import pandas as pd
import matplotlib.pyplot as plt
class ResidualSugar(): # intentionally not subclassing pd.DataFrame for simplicity
   def __init__(self, dataframe, colname, units='g_dm3'):  # constructor
      self.dataframe = dataframe
      self.colname = colname
      self.units = units
      # ml_per_serve = 150

   def __str__(self):  # to-string method
       return self.colname + " is reported as " + str(self.units) + "\n"
   
   def convert_to_gmL(self):
       # converts to g/mL
       dfcolumn=self.dataframe[self.colname]
       if self.units=='g_mL': # no change if units already g_mL
           rs_gmL = dfcolumn 
       if self.units=='g_l' or self.units=='g_dm3': # divide  by 1000 if g/L or g/dm3
           rs_gmL = dfcolumn / 1000
       self.dataframe['rs_gmL']=rs_gmL
            
   def convert_to_gdm3(self):
       # converts to g/dm3 (= g/L)
       dfcolumn=self.dataframe[self.colname]
       if self.units=='g_mL': # 
           rs_gdm3 = dfcolumn * 1000
       if self.units=='g_l' or self.units=='g_dm3':  # 1 g/l = 1 g/dm3
           rs_gdm3 = dfcolumn
       self.dataframe['rs_gdm3']=rs_gdm3
       
   def convert_to_gserve(self):
       # converts to gram per serving
       dfcolumn=self.dataframe[self.colname]
       if self.units=='g_l' or self.units=='g_dm3': # 150 ml in a serving
           rs_serve = dfcolumn * 150/1000  
       if self.units=='g_mL':
           rs_serve = dfcolumn * 150
       self.dataframe['rs_serve']=rs_serve

   def classify_sugar(self, scheme):
      # classifies wine based on sugar content
       if self.units != 'g_dm3' or self.units != 'g_l':
           self.convert_to_gdm3()
       dfcolumn=self.dataframe['rs_gdm3']
       newcol = dfcolumn.copy()
       # US classification scheme (from Wine Folly)
       if scheme=='US':
           bins = [0, 1, 17, 35, 120, 9999]
           labels = ['Bone Dry', 'Dry', 'Off-Dry', 'Sweet', 'Very Sweet']
           newcol_name='rs_type_US'
       # EU classification scheme (from Wikipedia)
       if scheme=='EU':
           bins = [0, 4, 12, 45, 9999]
           labels = ['Dry', 'Medium-Dry', 'Medium', 'Sweet']
           newcol_name='rs_type_EU'           
       newcol = pd.cut(self.dataframe['rs_gdm3'], bins=bins, labels=labels)
       self.dataframe[newcol_name]=newcol
       
   def boxplot_quality(self, attribute, ylabel="", title="", figsize=(6,4)):
       # creates boxplot of wine quality (x) vs attribute (y)
       if ylabel=="":
           ylabel = attribute
       bp = self.dataframe.boxplot(column=attribute, by='quality', grid=False, figsize=figsize)
       bp.set_xlabel("wine quality")
       bp.set_ylabel(ylabel)
       plt.title(title)
       plt.suptitle("")
       return plt.show()

   def boxplot_attrBin(self, attribute, bins, labels, xlabel="", title="", figsize=(6,4)):
       if xlabel=="":
           xlabel = attribute
       newcol = attribute + 'Bin'
       self.dataframe[newcol] = pd.cut(self.dataframe[attribute], bins=bins, labels=labels)
       bp = self.dataframe.boxplot(column='quality', by=newcol, grid=False, figsize=figsize)
       bp.set_xlabel(xlabel)
       bp.set_ylabel("wine quality")
       plt.title(title)
       plt.suptitle("")
       return plt.show()
       
        
   

 
 
 
 
 
 
 
 
 
       