#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Import modules 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#Set paramaters 
plt.rcParams['figure.dpi'] = 300
sns.set_theme(style="white")

#Read data 
df=pd.read_csv("merged_data.csv")


#Group data by race to see what race is most likely to be pulled over 
race= df.groupby('driverrace')
race_counts = race.size()
print(race_counts)
plt.figure(figsize=(12, 10)) 
# Plotting the bar graph for race 

plt.bar(race_counts.index, race_counts.values)
plt.tight_layout()
# Adding labels and title
plt.xlabel('Drivers Race')
plt.ylabel('Number of individuals pulled over ')
plt.title('Number of interactions by Drivers Race from 2010-2020' )

# Rotating x-axis labels for better readability
plt.xticks(rotation=90)

plt.savefig('race')
# Displaying the plot
plt.show()


# Group data by station to see where individuals are being pulled over 
station= df.groupby('stationname')
station_counts = station.size()
print(station_counts)

# Plotting the bar graph for station 

plt.bar(station_counts.index, station_counts.values)
plt.tight_layout()
# Adding labels and title
plt.xlabel('Station Name')
plt.ylabel('Count')
plt.title('Number of interactions for each station from 2010-2020' )

# Rotating x-axis labels for better readability
plt.xticks(rotation=90)

plt.savefig('station name')
# Displaying the plot
plt.show()


#Group data by  month to see when the highest amount of individuals are being pulled over 
month=df.groupby('month')
month_count=month.size()
print(month_count)

# Plotting the bar graph for month

plt.bar(month_count.index, month_count.values)
plt.tight_layout()
# Adding labels and title
plt.xlabel('Month' )
plt.ylabel('Number of individuals pulled over ')
plt.title('Number of interactions by Month from 2010-2020' )

# Rotating x-axis labels for better readability
plt.xticks(rotation=90)

plt.savefig('month')
# Displaying the plot
plt.show()



#Group data to see if there was a use of force in the interaction
force=df.groupby('useofforce')
force_count=force.size()
print(force_count)
# Plotting the bar graph for month

plt.bar(force_count.index, force_count.values)
plt.tight_layout()
# Adding labels and title
plt.xlabel('Month' )
plt.ylabel('Number interactions that resulted in force')
plt.title('Number of interactions that lead to a use of force from 2010-2020' )

# Rotating x-axis labels for better readability
plt.xticks(rotation=90)

plt.savefig('force')
# Displaying the plot
plt.show()


statutename=df.groupby('statutename')
statutename_count=statutename.size()
print(statutename_count)





