
import pandas as pd
import requests

# Gathering data from API
def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        print(f"Failed to retrieve data from API: {api_url}")
        return None

# List of API URLs
api_urls = [
    "https://data.nj.gov/resource/kie7-5sud.json" #2020,
    "https://data.nj.gov/resource/u3ag-s7w6.json" #2019,
    "https://data.nj.gov/resource/ui6b-hyzq.json" #2018,
    "https://data.nj.gov/resource/q8ec-3etm.json" #2017,
    "https://data.nj.gov/resource/weuz-d4x6.json" #2016,
    "https://data.nj.gov/resource/j2rb-g65t.json" #2015,
    "https://data.nj.gov/resource/vv5d-7trv.json" #2014,
    "https://data.nj.gov/resource/xz8t-a4ug.json" #2013,
    "https://data.nj.gov/resource/yugt-4yp9.json" #2012,
    "https://data.nj.gov/resource/9qfp-48xj.json" #2011,
    "https://data.nj.gov/resource/x8x7-g8dg.json" #2010
]

# Collecting data from the urls to be placed in data frames 
dataframes = []
for api_url in api_urls:
    df = fetch_data(api_url)
    if df is not None:
        dataframes.append(df)

# Merge data to one data set/csv file to then interpret data 
merged_df = pd.concat(dataframes, ignore_index=True)
merged_df.to_csv("merged_data.csv", index=False)
# Print first few rows of the merged dataframe
print(merged_df.head())
