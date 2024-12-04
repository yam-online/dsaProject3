# from ANALYSIS.PY, reformatted for tkinter

import pandas as pd
from math import sqrt
from idSimilarity import idSimilarity
from heapsort import heapsort
from quicksort import quicksort
from difflib import get_close_matches
from math import sqrt

movieData = pd.read_csv('data/u.item', sep='|', encoding='latin-1', header=None)
ratingData = pd.read_csv('data/item_avg.tsv', sep='\t', encoding='latin-1', header=None).iloc[:, 1]

# extract genre columns from movieData
genreData = movieData.iloc[:, 5:]
movieTitles = movieData.iloc[:, 1].str.lower().tolist()

# gets the closest movie title to a given string
def findClosestMovie(userInput):
    matches = get_close_matches(userInput, movieTitles, n=1, cutoff=0.8)
    return matches[0] if matches else None


# checks if the inputted rating is valid
def isValidRating(string):
    try:
        val = float(string)
        if (val <= 5 and val >= 0):
            return True
    except:
        return False

# returns whether or not the provided string is a valid user input for num of recommendations
def isValidNumber(string):
    try:
        val = int(string)
        if (val <= 15 and val >= 1):
            return True
    except:
        return False

# cosine similarity algorithm
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

# find similar movies, heapsort, quicksort
def similarMovies(movieTitle, minRating, rec):
    selectedId = movieTitles.index(movieTitle) + 1
    minRating = minRating
    recommendations = rec
    movies = []

    for id in movieData.iloc[:, 0]:
        if (id == selectedId): continue

        similarity = cosSim(selectedId, id)
        idSimObj = idSimilarity(id, similarity)
        movies.append(idSimObj)

    heapsort(movies)
    # quicksort(movies, 0, len(movies) - 1)

    recMoviesList = []

    count = 0 # number of recommendations made
    while count != recommendations and len(movies) > 0:
        titles = movieTitles
        top = movies.pop()

        if ratingData[top.id - 1] >= minRating:
            count += 1
            recMoviesList.append(f'{count}. "{titles[top.id - 1].capitalize()}" ● Rating: {ratingData[top.id - 1]:.2f} ● Similarity: {top.similarity:.3f}\n')

    return recMoviesList
# from ANALYSIS.PY, reformatted for tkinter