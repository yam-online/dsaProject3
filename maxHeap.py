from idGenre import idGenre

class maxHeap:

  # construct the max heap
  def __init__(self):
    self.movies = []

  # insert something into the max heap
  def insert(self, idGenreObj):
    self.movies.append(idGenreObj)
    self.heapifyUp()

  # call heapify up in insert() to maintain max heap properties
  def heapifyUp(self):
    child = len(self.movies) - 1
    parent = (child - 1) // 2
    while parent >= 0 and self.movies[parent].movieGenre < self.movies[child].movieGenre:
      self.movies[parent], self.movies[child] = self.movies[child], self.movies[parent]
      child = parent
      parent = (child - 1) // 2
