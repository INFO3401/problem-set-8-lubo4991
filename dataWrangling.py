#Lucas Bouchard



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
    df['comment_msg'].drop(['app', 'free', '%20', 'check out my page', 'www.', 'http://'])

    #Problem 3: clean Null values
    df = df[df['comment_msg'] != ""]

    df.to_csv(output_file)

generateCleanFile("dd-comment-profile.csv", "cleaned-dd-comment-profile111.csv")