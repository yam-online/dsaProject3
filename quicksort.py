def partition(arr, lo, hi):
    # pivot selection is arbitrary in our case, so we simply pick the last element
    pivot = arr[hi]
    ptr = lo

    for i in range(lo, hi):
        if arr[i].similarity <= pivot.similarity:
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
            
    arr[ptr], arr[hi] = arr[hi], arr[ptr]
    return ptr

# basic iterative quicksort implementation
# best case time:   O(nlogn)
# worst case time:  O(n^2)
# best case space:  O(logn)
# worst case space: O(n^2)
def quicksort(arr, lo, hi):
    stack = [(lo, hi)]

    while stack:
        lo, hi = stack.pop()

        if lo < hi:
            pivot = partition(arr, lo, hi)
            stack.append((lo, pivot - 1))
            stack.append((pivot + 1, hi))
