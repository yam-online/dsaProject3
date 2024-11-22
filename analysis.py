import pandas as pd

movieData = pd.read_csv('data/u.item', sep='|', encoding='latin-1')
# print(movieData.head())

ratingData = pd.read_csv('data/u.data', sep='\t')
# print(ratingData.head())