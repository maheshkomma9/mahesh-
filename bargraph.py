#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 13:42:29 2023

@author: maheshkomma
"""
#import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

'''Fetch the data in excel sheet by using pandas and store it in a variable'''
Anual_Rainfall_Report = pd.read_excel('/Users/maheshkomma/Downloads/Book (6).xlsx')
print(Anual_Rainfall_Report)


#plot the data into a bar graph and eclaring the colors
Anual_Rainfall_Report.plot.bar(x = "Months", color = ['blue', 'orange', 'green'],
                               figsize = (12, 8)) 

#labelling the plot
plt.title("Monthly Average Rainfall in UK \n From Past Three Years", 
          fontsize = (25), color = 'cadetblue') #title

plt.xlabel("Months", fontsize = (15), color = 'slategrey') #x-axis
plt.ylabel('Rainfall in mm', fontsize = (15), color = 'slategrey') #y-axis

#change the view of x axis elements
plt.xticks(rotation = 40)
plt.show()