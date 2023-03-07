# pip install pandas-profiling

import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)


import pandas as pd 
from pandas_profiling import ProfileReport 


# 1. Read the CSV File
df = pd.read_csv("./output_my_data.csv")


# 2. Create a Profile
profile = ProfileReport(df)



# 3. Save the output profile 
profile.to_file(output_file = "./profile.html")