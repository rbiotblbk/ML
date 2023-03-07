# Python 3.10 -> Python 3.11 (not yet)

# pip install pandas-profiling (old version till 1st April 2023)
# pip install ydata-profiling (new version)


import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)


import pandas as pd 

# Old Version
#~~~~~~~~~~~~~~
#from pandas_profiling import ProfileReport # (old version till 1st April 2023)

# New Version
#~~~~~~~~~~~~~~
from ydata_profiling import ProfileReport # (new version)

# 1. Read the CSV File
df = pd.read_csv("./output_my_data.csv")


# 2. Create a Profile
profile = ProfileReport(df)



# 3. Save the output profile 
profile.to_file(output_file = "./profile.html")