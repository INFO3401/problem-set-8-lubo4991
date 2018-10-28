
import string
import os
from os import listdir
import csv


#https://stackoverflow.com/questions/17176542/remove-specific-character-from-a-csv-file-and-rewrite-to-a-new-file

def generateCleanFile(input_file, output_file):
    in_file= open(input_file, 'rb')
    lines= csv.reader(in_file)
    out_file= open(output_file, 'wb')
    writer= csv.writer(out_file)
  
    characters = ['<.*?>', '\r*','app', 'free', '%20', 'check out my page', 'www.', 'http://']

    for line in lines:
        line = str(line)
        new_line = str.replace(line,characters,'')
        writer.writerow(new_line.split(','))

    input_file.close()
    output_file.close()

generateCleanFile("dd-comment-profile.csv", "cleaned-dd-comment-profile.csv")