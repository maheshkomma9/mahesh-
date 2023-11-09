#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

#create the data frame and store the data
Pie_chart_data = pd.DataFrame({'without_travelcard_and_clubcards':[250,100,
                                                135,80,120,300,120,100,215],
                 'with_travelcard_and_clubcard':[220,80,100,55,90,300,120,
                                                 100,355]}, 
                  index = ['Transport','Groceries','Shoping','Entertainment',
                        'Eating out','Rent','Loan','Bills','Savings'])

print(Pie_chart_data)

#plot the graph
Pie_chart_data.plot.pie(subplots = True, labels = (Pie_chart_data.index), 
                        autopct = '%1.1f%%', startangle = 50, figsize = (15,8))

#labelling the plot
plt.suptitle('''Difference between monthly expenses with usage 
             of travelcards and clubcards in UK''', fontsize = 18, color = 'tomato')
plt.legend()