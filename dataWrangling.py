#Lucas Bouchard

#sources:
#https://chrisalbon.com/python/data_wrangling/pandas_dropping_column_and_rows/
#https://stackoverflow.com/questions/31663426/python-pandas-drop-rows-from-data-frame-on-string-match-from-list/31663495


import pandas as pd
import csv

def generateCleanFile(input_file, output_file):
    df = pd.read_csv(input_file, low_memory=False, encoding="latin1")

    #Problem 2: Clean HTML and whitespace
    
    df['comment_msg'] = df['comment_msg'].str.strip()
    df['comment_msg'] = df['comment_msg'].str.lower()
    df['comment_msg'] = df['comment_msg'].replace(r'\r*', '', regex=True)
    df['comment_msg'] = df['comment_msg'].replace(r'<.*?>', '', regex=True)


  #Problem 1: Clean spam
    drop= ['app', 'free', '%20', 'check out my page', 'www.', 'http://']
    #df[df['comment_msg'].isin(drop)]
    df[df['comment_msg'].str.contains('|'.join(drop), na=False)]
    
  #Problem 3: clean Null values
        #CANT GET THESE TO WORK. IT STILL GENERATES A FILE WITH BLANK ROWS..I've tried 5 different methods and nothing works. 
    df2=df[pd.notnull(df['comment_msg'])]
    #df.dropna(subset=['comment_msg'], inplace = True)
    df2.to_csv(output_file)


generateCleanFile("dd-comment-profile.csv", "cleaned-dd-comment-profile.csv")