"""
test
"""
import io
import pandas as pd
import requests


# Downloading the csv file from your GitHub

url = "https://raw.githubusercontent.com/YaoYuanxin/remote_private_data/main/penguins_cleaned.csv?token=GHSAT0AAAAAAB2W6ITHGLEVOSBZVDXGLHGGY4JFV7A"
download = requests.get(url).content

# Reading the downloaded content and making it a pandas dataframe

df = pd.read_csv(io.StringIO(download.decode('utf-8')))

# Printing out the first 5 rows of the dataframe to make sure everything is good

print (df.head())
df.to_csv("peguine_data.csv")
