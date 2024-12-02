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
from quicksort import quicksort
from difflib import get_close_matches
from idSimilarity import idSimilarity
from adjacencyList import adjacencyList

movieData = pd.read_csv('data/u.item', sep='|', encoding='latin-1', header=None)
ratingData = pd.read_csv('data/item_avg.tsv', sep='\t', encoding='latin-1', header=None).iloc[:, 1]

# extract genre columns from movieData
genreData = movieData.iloc[:, 5:]
movieTitles = movieData.iloc[:, 1].str.lower().tolist()

'''
JACK GORDON: you can do the cosine algorithm here
if you are doing a for loop through all the data points (genreData), create an idSimilarity object for each data point so we can group together an id and a genre-match-ranking-number for each 
'''

# gets the closest movie title to a given string
def findClosestMovie(userInput):
    matches = get_close_matches(userInput, movieTitles, n=1, cutoff=0.6)
    return matches[0] if matches else None

# returns the id associated with the user inputted title
def getMovieId():
    inputTitle = input("Enter a movie title: ").lower()
    title = findClosestMovie(inputTitle)

    # input validation
    while title is None:
        inputTitle = input("No movie found, please enter a new title: ").lower()
        title = findClosestMovie(inputTitle)

    selectedId = movieTitles.index(title) + 1
    return selectedId

# checks if the inputted rating is valid
def isValidNumber(string):
    try:
        val = float(string)
        return (val <= 5 and val >= 0)
    except:
        return False

# returns the user inputted minimum rating
def getRatingInput():
    minRating = input("Enter a minimum required rating (0-5): ")
    
    while not isValidNumber(minRating):
        minRating = input("Invalid rating, try again (0-5): ")

    return float(minRating)
    

# cosine similarity algorithm
# dot product is commutative, so id1 and id2 have no specific order they need to be put in as
def cosSim(id1, id2):
    # ids are 1 indexed, the table is 0 indexed.
    vector1 = genreData.iloc[id1 - 1]
    vector2 = genreData.iloc[id2 - 1]
    dotProduct = sum1 = sum2 = 0

    # because we know our data only contains 0 or 1 for the vector entries   (whose squares are themselves 0 or 1 respectively)
    # we can just use a normal sum instead of a sum of sqaures for finding the magnitude at then end, as theyll be the same
    
    for component1, component2 in zip(vector1, vector2):
        dotProduct += component1 * component2
        sum1 += component1
        sum2 += component2

    similarity = dotProduct / sqrt(sum1) / sqrt(sum2)
    return similarity

# BEGIN PROGRAM FLOW
selectedId = getMovieId()
minRating = getRatingInput()
movieHeap = maxHeap()

for id in movieData.iloc[:, 0]:
    if (id == selectedId): continue

    similarity = cosSim(selectedId, id)
    idSimObj = idSimilarity(id, similarity)
    movieHeap.insert(idSimObj)

recommendations = 10 # number of recommendations to make
count = 0 # number of recommendations made
movieHeap.heapSort()
# quicksort(movieHeap.movies, 0, len(movieHeap.movies) - 1)
while count != recommendations and len(movieHeap.movies) > 0:
    titles = movieTitles
    top = movieHeap.movies.pop()

    if ratingData[top.id - 1] >= minRating:
        count += 1
        print(titles[top.id - 1], "\nRating:", ratingData[top.id - 1], "\nSimilarity:", top.similarity, "\n")