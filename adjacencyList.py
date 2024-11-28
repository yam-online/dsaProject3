from idSimilarity import idSimilarity

class adjacencyList:
  # construct the adjacency list
  def __init__(self):
    self.movies = {}

  # insert an idSimilarity object into adjacency list
  def insert(self, inputId, similarMovie):
    if inputId not in self.movies:
      self.movies[inputId] = []
    # only make it an adjacent node if its similarity factor > 0.8
    if similarMovie.similarity > 0.8:
      self.movies[inputId].append(similarMovie)