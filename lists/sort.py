def insertionsort(A):
    """Sort a list in place by insertion sort"""
    for i in range(len(A)):
        key = A[i]
        j = i-1
        # for j < i, if A[j] > A[i] then move A[j] over to the right
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        # insert A[i] when all larger elements are moved over
        A[j+1] = key

def bubblesort(A):
    """sort a list in place by bubble sort"""
    for i in reversed(range(1,len(A))):
        # for j = 1 up to i+1, swap A[j] and A[j-1] if out of order
        for j in range(1,i+1):
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]

