Lucas Bouchard




import string
import os
from os import listdir
import csv


https://stackoverflow.com/questions/17176542/remove-specific-character-from-a-csv-file-and-rewrite-to-a-new-file

def generateCleanFile(input_file, output_file):
    old_file = open(input_file, 'r')
    new_file open(output_file, 'w')
    #input_file = open('DesktopData.csv', 'r')
    #output_file = open('fixformat.csv', 'w')
    data = csv.reader(old_file)
    writer = csv.writer(new_file)
    specials = ['<', '>']

for line in data:
    line = str(line)
    new_line = str.replace(line,specials,'')
    writer.writerow(new_line.split(','))

input_file.close()
output_file.close()

generateCleanFile("dd-comment-profile.csv", "cleaned-dd-comment-profile.csv")