from idSimilarity import idSimilarity

class adjacencyList:
  # construct the adjacency list
  def __init__(self, inputId):
    self.movies = {inputId : []}

  # insert an idSimilarity object into adjacency list
  def insert(self, inputMovie, similarMovie):
    # only make it an adjacent node if its similarity factor > 0.8
    if similarMovie.similarity > 0.8:
      self.movies[inputMovie].append(similarMovie)