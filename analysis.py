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
from maxHeap import maxHeap
from idGenre import idGenre

movieData = pd.read_csv('data/u.item', sep='|', encoding='latin-1')

# extract genre columns from movieData
genreData = movieData.iloc[:, 5:]

ratingData = pd.read_csv('data/u.data', sep='\t')

# extract only movie id and ratings from ratingData
ratingData = ratingData.iloc[:, 1:3]

'''
JACK GORDON: you can do the cosine algorithm here
if you are doing a for loop through all the data points (genreData), create an idGenre object for each data pointso we can group together an id and a genre-match-ranking-number for each 
'''

# test = maxHeap()
# obj1 = idGenre(0, 1)
# obj2 = idGenre(1, 3)
# obj3 = idGenre(2, 5)
# obj4 = idGenre(3, 4)
# obj5 = idGenre(4, 6)
# obj6 = idGenre(5, 13)
# obj7 = idGenre(6, 10)
# obj8 = idGenre(7, 9)
# obj9 = idGenre(8, 8)
# obj10 = idGenre(9, 15)
# obj11 = idGenre(10, 17)


# test.insert(obj1)
# test.insert(obj2)
# test.insert(obj3)
# test.insert(obj4)
# test.insert(obj5)
# test.insert(obj6)
# test.insert(obj7)
# test.insert(obj8)
# test.insert(obj9)
# test.insert(obj10)
# test.insert(obj11)

# test.heapifyUp()

# for i in test.movies:
#   print(f'{i.id} + {i.movieGenre}')
# print('\n')