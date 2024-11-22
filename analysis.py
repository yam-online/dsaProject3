import csv
import pandas as pd

# input = 'data/u.item'
# output = 'data/movieData.csv'

# # rewrite as csv file
# with open(input, 'r') as infile, open(output, 'w', newline='') as outfile:
#   csv_writer = csv.writer(outfile)

#   for line in infile:
#     csv_writer.writerow(line.strip().split('|'))

# print('hello')



# import chardet

# with open('data/u.tsv', 'rb') as f:
#   result = chardet.detect(f.read())

# movieData = pd.read_csv('data/u.tsv', encoding=result['encoding'])