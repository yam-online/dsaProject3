''' 
sources:
1. https://stackoverflow.com/questions/5552555/unicodedecodeerror-invalid-continuation-byte
2. https://www.geeksforgeeks.org/heap-sort/
3.
'''

'''
HEMANSHU BOPPANA: you can create the adjacency list/matrix as a class
'''

import pandas as pd
from math import sqrt
from maxHeap import maxHeap
from idSimilarity import idSimilarity
from adjacencyList import adjacencyList

movieData = pd.read_csv('data/u.item', sep='|', encoding='latin-1', header=None)

# extract genre columns from movieData
genreData = movieData.iloc[:, 5:]

ratingData = pd.read_csv('data/u.data', sep='\t', header=None)

# extract only movie id and ratings from ratingData
ratingData = ratingData.iloc[:, 1:3]

'''
JACK GORDON: you can do the cosine algorithm here
if you are doing a for loop through all the data points (genreData), create an idSimilarity object for each data point so we can group together an id and a genre-match-ranking-number for each 
'''

# cosine similarity algorithm
# dot product is commutative, so id1 and id2 have no specific order they need to be put in as
def cosSim(id1, id2):
    # ids are 1 indexed, the table is 0 indexed.
    vector1 = genreData.iloc[id1 - 1]
    vector2 = genreData.iloc[id2 - 1]
    dotProduct = sum1 = sum2 = 0

    # because we know our data only contains 0 or 1 for the vector entries (whose squares are themselves 0 or 1 respectively)
    # we can just use a normal sum instead of a sum of sqaures for finding the magnitude at then end, as theyll be the same
    
    for component1, component2 in zip(vector1, vector2):
        dotProduct += component1 * component2
        sum1 += component1
        sum2 += component2

    similarity = dotProduct / sqrt(sum1) / sqrt(sum2)
    return similarity

# TODO: Replace this placeholder with user-inputted movie id
inputId = 1
movieHeap = maxHeap()

for id in movieData.iloc[:, 0]:
    if (id == inputId): continue

    similarity = cosSim(inputId, id)
    idSimObj = idSimilarity(id, similarity)
    movieHeap.insert(idSimObj)

# TESTING adjacency lit
inputId = 49
movieGraph = adjacencyList(inputId)

for id in movieData.iloc[:, 0]:
    if (id == inputId): continue

    similarity = cosSim(inputId, id)
    idSimObj = idSimilarity(id, similarity)
    movieGraph.insert(inputId, idSimObj)

for v in movieGraph.movies:
  for similar in movieGraph.movies[v]:
      print(similar.similarity)
# TESTING adjacency list

# TESTING TESTING TESTING TESTING TESTING TESTING TESTING TESTING TESTING
# movieHeap.heapSort()
# for i in range(10):
#     names = movieData.iloc[:, 1]
#     top = movieHeap.movies.pop()
#     print(names[top.id - 1], top.similarity)
# print('\n')

# Toy Story:                0|0|0|1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0
# ---------------------------------------------------------------
# Aladdin & the King:       0|0|0|1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0
# Aladdin:                  0|0|0|1|1|1|0|0|0|0|0|0|1|0|0|0|0|0|0
# Goofy Movie:              0|0|0|1|1|1|0|0|0|0|0|0|0|0|1|0|0|0|0
# TESTING TESTING TESTING TESTING TESTING TESTING TESTING TESTING TESTING


# TESTING heap sort
# test = maxHeap()
# obj1 = idSimilarity(0, 1)
# obj2 = idSimilarity(0, 2)
# obj3 = idSimilarity(0, 3)
# obj4 = idSimilarity(0, 4)
# obj5 = idSimilarity(0, 5)
# obj6 = idSimilarity(0, 6)
# obj7 = idSimilarity(0, 7)

# test.insert(obj1)
# test.insert(obj2)
# test.insert(obj3)
# test.insert(obj4)
# test.insert(obj5)
# test.insert(obj6)
# test.insert(obj7)

# test.heapSort()

# for i in test.movies:
#   print(f'{i.id} + {i.similarity}')
#   print('\n')
# TESTING heap sort