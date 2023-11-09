#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:45:41 2023

@author: maheshkomma
"""
#import the necessary Libraries
import pandas as pd
import matplotlib.pyplot as plt

'''Fetch the excel data sheet and use the apropriate function to read data'''
#creating a variable to store the data frame
Countries_QLI_data = pd.read_excel('/Users/maheshkomma/Downloads/Book 4.xlsx')
print(Countries_QLI_data)

#Plot the data by declaring the axis and marker style and color
Countries_QLI_data.plot(x = 'Year', marker = 's')

#labelling the line plot
plt.title('''Comparision of Quality of Life
          Index between five different countries''', color = 'darkkhaki')
plt.xlabel('Year', color = 'olivedrab', size = 12)

#add the grid view to the plot
plt.grid(True)
plt.grid(which = 'major', color = '#dddddd', linewidth = 0.8) 
plt.grid(which = 'minor', color = '#EEEEEE', linewidth = 0.5)
plt.minorticks_on()

#change the view of elements on x
plt.xticks(rotation = 40)
plt.show()