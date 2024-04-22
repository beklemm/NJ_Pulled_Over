# NJ_Pulled_Over

# Summary 
This code will interpret demographic data about who is getting pulled over in NJ. The aim of this project is to be a tool for individuals to understand potential basis that could effect them.
# Input Data 
This repository utlises api codes from NJ State Open Data Portal, entitiled NJSP Traffic Stop Data. For easy completion of this code, it would be of value to collect api urls from 2010-2020

# Instructions
## A. get_data.py
1. import pandas as pd 
1. import requests
1. Go on url "https://data.nj.gov/browse?q=NJSP%20Traffic%20Stop%20Data%202010&sortBy=relevance" to collect API urls for NJSP Traffic Stop Data 2010-2020
1. Place collected urls in a list titled "api_urls"
1. We will now begin the process of collecting the data from the API urls and covert them to dataframes 
    1. Create an empty list titled "dataframes" 
    1. Create a for loop through elements "api_url" in the "api_urls" list 
    1. Within the loop create variable "df" and use the fetch data funtion on the "api_url". Example "df = fetch_data(api_url)"
    1. Check to see the loop collected data by using an if statment with the condition "if df is not None" with the result using the append method to the dataframes list. This will add the the data to the existing dataframe. 
1. Using the concat method on varibale "merged_df" with the conditions dataframes and ignore_index=True
1. Covert this merged data into a csv using "merged_df.to_csv" with the conditions ("merged_data.csv", index=False)
1. Check to make sure everything merged correctly by using the .head fuction which will output the first 5 rows of your merged data set 

## B. demographic_pull_over.py
1. import pandas as pd 
1. import seaborn as sns 
1. import matplotlib as plt
1. In order to properly understand this data we will now repeat a series of identical  steps on variables "driverrace", "stationname", "month", and "force". By completeing these steps we will be able to get a picture of race, what station is the interaction taking place, what month this is taking place and if there was a use of force durring the interaction. 
    1. Create variable reflecting the variable and call the .groupby() method on your varaible 
    1. Create a variable_count where you call .size() method on your previous variable 
    1. print your variable from previous step to see the disparties 