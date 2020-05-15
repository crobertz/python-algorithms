def binarysearch_slice(A, target):
    """given a sorted array A checks if target is in A using list slicing"""
    if not A:
        return "Target not found."
    index = len(A) // 2
    mid = A[index]
    if mid == target:
        return "Target found."
    if len(A) == 1:
        return "Target not found."
    else:
        if mid < target:
            return binarysearch_slice(A[index:], target)
        else:
            return binarysearch_slice(A[:index], target)

def binarysearch(A, target):
    """given a sorted array A check if target is in A and return index for target"""
    index = len(A) // 2
    increment = index

    while increment > 0:
        increment = increment // 2
        if A[index] == target:
            return "Target found at {}.".format(index)
        if A[index] < target:
            index += increment
        else:
            index -= increment
    
    # since floor(floor(x/b)/a) = floor(x/(ab)) can be off by at most 1
    for j in [-1,0,1]:
        if index + j >= 0 and index + j < len(A):
            if A[index + j] == target:
                return "Target found at {}.".format(index + j)
    
    return "Target not found."


print(binarysearch([1,2,3,4,5,6,7,8], 1))