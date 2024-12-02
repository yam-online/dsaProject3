import pandas as pd
from math import sqrt
from difflib import get_close_matches

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

# # returns the id associated with the user inputted title
# def getMovieId():
#     inputTitle = input("Enter a movie title: ").lower()
#     title = findClosestMovie(inputTitle)

#     # input validation
#     while title is None:
#         inputTitle = input("No movie found, please enter a new title: ").lower()
#         title = findClosestMovie(inputTitle)

#     selectedId = movieTitles.index(title) + 1
#     return selectedId

def getMovieId(userInput):
    inputTitle = userInput.lower()
    title = findClosestMovie(inputTitle)

    # input validation
    if title is None:
        return None

    return title


# checks if the inputted rating is valid
def isValidRating(string):
    try:
        val = float(string)
        return (val <= 5 and val >= 0)
    except:
        return False

# returns the user inputted minimum rating
def getRatingInput():
    minRating = input("Enter a minimum required rating (0-5): ")
    
    while not isValidRating(minRating):
        minRating = input("Invalid rating, try again (0-5): ")

    return float(minRating)

# returns whether or not the provided string is a valid user input for num of recommendations
def isValidNumber(string):
    try:
        val = int(string)
        return (val <= 20 and val >= 1)
    except:
        return False