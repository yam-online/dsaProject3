from idSimilarity import idSimilarity

# standard heapify down
def heapifyDown(movies, size, root):
    parent = root

    while True:
      left = 2 * parent + 1
      right = 2 * parent + 2
      largest = parent

      if left < size and movies[left].similarity > movies[largest].similarity:
        largest = left

      if right < size and movies[right].similarity > movies[largest].similarity:
        largest = right

      if largest == parent:
        break

      movies[parent], movies[largest] = movies[largest], movies[parent]
      parent = largest

# basic heap sort
# best case time:   O(nlogn)
# worst case time:  O(nlogn)
# best case space:  O(1)
# worst case space: O(1)
def heapsort(movies):
  size = len(movies)

  # build the heap
  for i in range(size // 2 - 1, -1, -1):
    heapifyDown(movies, size, i)

  # sort the heap
  for i in range(size - 1, -1, -1):
    movies[0], movies[i] = movies[i], movies[0]
    heapifyDown(movies, i, 0)