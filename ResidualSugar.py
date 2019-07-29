#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
#import pandas as pd
class ResidualSugar(): # intentionally not subclassing pd.DataFrame for simplicity
   def __init__(self, dataframe, colname, units='g_dm3', oz_per_mL3=0.033814):  # constructor
      self.dataframe = dataframe
      self.colname = colname
      self.units = units
      self.oz_per_mL3 = oz_per_mL3 # 0.033814
#      oz_per_serve = 5
#      ml_per_serve = 150

   def __str__(self):  # to-string method
       return self.colname + " is reported as " + str(self.units) + "\n"
   
   def convert_to_gdm3(self):
       # converts to g/dm3
       dfcolumn=self.dataframe[self.colname]
       if self.units=='g_oz': # 33.81402 g/oz = 1 g/dm3
           rs_gdm3 = dfcolumn * self.oz_per_mL3 * 1000
       if self.units=='g_l' or self.units=='g_dm3': # 1 g/l = 1 g/dm3
           rs_gdm3 = dfcolumn
       self.dataframe['rs_gdm3']=rs_gdm3
          
   def convert_to_goz(self):
       # converts to g/oz
       dfcolumn=self.dataframe[self.colname]
       if self.units=='g_oz':       # 1 g/oz = 1 g/oz
           rs_goz = dfcolumn
       if self.units=='g_l' or self.units=='g_dm3': # 1 g/l= 33.81402 g/oz
           rs_goz = dfcolumn / (self.oz_per_mL3 * 1000)
       self.dataframe['rs_goz']=rs_goz       
          
   def convert_to_gserve(self):
       # converts to gram per serving
       dfcolumn=self.dataframe[self.colname]
       if self.units=='g_oz':        # 5 oz in a serving
           rs_serve = dfcolumn * 5
       if self.units=='g_l' or self.units=='g_dm3': # 150 ml in a serving
           rs_serve = dfcolumn * 150/1000    
       self.dataframe['rs_serve']=rs_serve

   def classify_sugar(self):
      # classifies wine based on sugar content
       if self.units != 'g_dm3' or self.units != 'g_l':
           self.convert_to_gdm3()
       dfcolumn=self.dataframe['rs_gdm3']
       newcol = dfcolumn.copy()    
       for row in range((len(newcol))):
           if newcol[row] < 1:
               newcol[row] = 'Bone Dry'
           elif newcol[row] >= 1 and newcol[row] < 17:
               newcol[row] = 'Dry'           
           elif newcol[row] >= 17 and newcol[row] < 35:
               newcol[row] = 'Off-Dry'
           elif newcol[row] >= 35 and newcol[row] < 120:
               newcol[row] = 'Medium-Sweet'
           elif newcol[row] >= 120:
               newcol[row] = 'Sweet'
       self.dataframe['rs_type']=newcol
   

 
 
 
 
 
 
 
 
 
       