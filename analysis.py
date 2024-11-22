import pandas as pd
from maxHeap import maxHeap


movieData = pd.read_csv('data/u.item', sep='|', encoding='latin-1')

# extract genre columns from movieData
genreData = movieData.iloc[:, 5:]

ratingData = pd.read_csv('data/u.data', sep='\t')

# extract only movie id and ratings from ratingData
ratingData = ratingData.iloc[:, 1:3]
