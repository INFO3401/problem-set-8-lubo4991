import string
import os
from os import listdir
import csv
import json




def generateCleanFile(cleaner, targetfile):
    input_file = open('DesktopData.csv', 'r')
    output_file = open('fixformat.csv', 'w')
    data = csv.reader(input_file)
    writer = csv.writer(output_file)
    specials = ['<', '>', ]

for line in data:
    line = str(line)
    new_line = str.replace(line,specials,'')
    writer.writerow(new_line.split(','))

input_file.close()
output_file.close()