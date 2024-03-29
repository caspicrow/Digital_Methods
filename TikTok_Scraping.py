"""
I first gathered 9 HAR files straight from the TikTok website, each with ~18 comments (as well as everything else loaded on the page)
I then converted the HAR files to JSON files via stevesie.com/apps/tiktok-api .
This code turns these JSON files into CSV files. 
NOTE: This does not include replies to comments.
"""

import json
import pandas as pd
import os
os.chdir(r"G:\My Drive\School\JAAR 2\3 - DIGITAL METHODS\CODE\TikTok 1")

file = open("raw_response.json", encoding="utf-8-sig") #encoding added as python couldn't read some cells otherwise?

#Reading the file
data = json.load(file)
comments = data["comments"]
df = pd.DataFrame(comments)

#removing columns that contain personal info
df.drop(columns = ["user", "share_info"])

df.to_csv("comments.csv", index=False)

#repeating this process for all json files
no = 1
while no <= 9:
    file = open(f"raw_response ({no}).json", encoding="utf-8-sig") #the files are called "raw_response (1)" etc.
    
    data = json.load(file)
    comments = data["comments"]
    print(comments)
    
    df = pd.DataFrame(comments)
    
    df.head()
    
    df.to_csv(f"comments{no}.csv", index=False)
    
    no += 1 #this makes the code move on to the next file until it reaches the last one.
    
"""
The code below merges all comment files into one dataframe and then CSV file called "TT_comments.csv".
I'm sure there are more efficient ways of doing this. I just can't think of any right now.
...I promise my code usually looks cleaner.
"""
file = "comments.csv"

with open(file, encoding="utf-8-sig"):
    df = pd.read_csv(file, sep=",")
    

file = "comments1.csv"

with open(file, encoding="utf-8-sig"):
    df1 = pd.read_csv(file, sep=",")
    
file = "comments2.csv"

with open(file, encoding="utf-8-sig"):
    df2 = pd.read_csv(file, sep=",")
    
file = "comments3.csv"

with open(file, encoding="utf-8-sig"):
    df3 = pd.read_csv(file, sep=",")
    
file = "comments4.csv"

with open(file, encoding="utf-8-sig"):
    df4 = pd.read_csv(file, sep=",")
    
file = "comments5.csv"

with open(file, encoding="utf-8-sig"):
    df5 = pd.read_csv(file, sep=",")
    
file = "comments6.csv"

with open(file, encoding="utf-8-sig"):
    df6 = pd.read_csv(file, sep=",")
    
file = "comments7.csv"

with open(file, encoding="utf-8-sig"):
    df7 = pd.read_csv(file, sep=",")
    
file = "comments8.csv"

with open(file, encoding="utf-8-sig"):
    df8 = pd.read_csv(file, sep=",")
    
file = "comments9.csv"

with open(file, encoding="utf-8-sig"):
    df9 = pd.read_csv(file, sep=",")
    
frames = [df, df1, df2, df3, df4, df5, df6, df7, df8, df9]
result = pd.concat(frames)

result.to_csv("TT_comments1.csv", sep=",", index=False)
