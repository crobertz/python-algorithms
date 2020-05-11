def parent(i):
    """given index i returns parent index"""
    return int((i-1)/2)

def left_child(i):
    """given index i returns left child index"""
    return 2 * i + 1

def right_child(i):
    """given index i returns right child index"""
    return 2 * (i + 1)

def max_heapify(A, i):
    """
    given array A such that the trees at left and right of i are heaps,
    turn tree rooted at i into a heap
    """
    l = left_child(i)
    r = right_child(i)
    if l < len(A) and A[l] > A[i]:
        largest_idx = l
    else:
        largest_idx = i
    if r < len(A) and A[r] > A[largest_idx]:
        largest_idx = r
    if largest_idx != i:
        A[largest_idx], A[i] = A[i], A[largest_idx]
        max_heapify(A,largest_idx)

def build_max_heap(A):
    """
    turn an array A into a max heap
    """
    for i in reversed(range(int(len(A)/2))):
        max_heapify(A, i)

def heapsort(A):
    """
    given A returns a sorted copy of A
    """
    sorted_list = [None] * len(A)
    build_max_heap(A)
    for i in reversed(range(len(A))):
        A[0], A[-1] = A[-1], A[0]
        sorted_list[i] = A.pop()
        max_heapify(A, 0)
    return sorted_list