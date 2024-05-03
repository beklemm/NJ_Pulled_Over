# NJ_Pulled_Over

# Summary 
This code will interpret demographic data about who is getting pulled over in NJ. The aim of this project is to be a tool for individuals to understand potential basis that could effect them.
# Input Data 
This repository utlises api codes from NJ State Open Data Portal, entitiled NJSP Traffic Stop Data. For easy completion of this code, it would be of value to collect api urls from 2010-2020
# Expected Output Files 
There are several output files. The python files are get_data.py and demographic_pull_over.py. From the output of the demographic_pull_over file completion, there should be 5 .png files from the graphs. Finally, there is the Tablaue file, User_Input.twb. 
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

## User_Input.twb 
1. Open Tableau Desktop 
1. Connect data file previously made called merged_data.csv 
    1. To connect data go in the 'To a File' section and select 'text file'
    1. Select the merged_data.csv file 
1. Go through the process of creating 4 sheets (each sheet hold a specific graph) that can be filtered by Year and Station Name 
    1. Sheet 1 (Number of Individuals Pulled Over by Race and Station )
        1. Drag variable  'Stationname' into the filter box 
        1. Right click and select 'Apply to Worksheets' and check off 'All using data source' 
        1. Right click on the blue box labeled 'Stationname' and select 'Show Filter' 
        1. Once filter pops up right click the right corner and select 'Single Value (dropdown)'. This will allow users to select a speicfic station to focus on. 
        1. Drag 'Stationname' from data collumn and place it in box labeled collumns 
        1. Drag 'Driverrace' from data collumn and place it in box labled rows 
        1. Right click 'Driverrace' on rows box and find Measure (count) and select count from list 
        1. Select the stagered bar graph
    1. Now we will make sheet 2  (number of arrest per month)
        1. Select the heat map on the show me right section and use arrest and month
    1. Now we will make sheet 3 (outcome of being pulled over)
        1.   Drag 'Stopoutcome' from data collumn and place it in box labeled collumns 
        1. Drag 'Stopoutcome' from data collumn and place it in box labled rows 
        1. Right click 'Stopoutcome' on rows box and find Measure (count) and select count from list 
        1. Select the bar graph
    1. Now we will make sheet 4 (Number of DWIs by Month)
       1.  Select the heat map on the show me right section and use Totaldwi and month
1. Now that the sheets are created we now will create a dashboard 
    1. Drag sheets from right hand side to the dashboard 
    1. Edit the titles by clicking on the text to make them representive 
    1. Once you are happy with the product, save the assignment. Then hit extract on the data source. 
    1. Upload assingment by selecting, sever, then tableau public and hit save. 
1. You can acess my interactive database at: https://public.tableau.com/views/User_Input/MAINDASHBOARD?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link

## Conclusion
This project aims to be a tool to understand the complexities interactions that take place when individuals are pulled over in NJ. This tool can be used for a vairety of purposes from understanding bais to program evalutation by station. 


    