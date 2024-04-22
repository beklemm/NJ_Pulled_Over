#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:59:40 2024

@author: baileyklemm
"""
#Import modules 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#Set paramaters 
plt.rcParams['figure.dpi'] = 300
sns.set_theme(style="white")

#Read data 
data=pd.read_csv("merged_data.csv")

#Group data by race to see what race is most likely to be pulled over 
race= data.groupby('driverrace')
race_counts = race.size()
print(race_counts)

# Group data by station to see where individuals are being pulled over 
station= data.groupby('stationname')
station_counts = station.size()
print(station_counts)

#Group data by  month to see when the highest amount of individuals are being pulled over 
month=data.groupby('month')
month_count=month.size()
print(month_count)

#Group data to see if there was a use of force in the interaction
force=data.groupby('useofforce')
force_count=force.size()
print(force_count)

