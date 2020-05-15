def binarysearch(A, target, left=0, right=len(A)-1):
    """Searches A for target and returns 'Found' if found and 'Not found' otherwise"""
    
    # base cases
    if not A:
        return 'Not found'
    if len(A) == 1:
        if A[0] == target:
            return 'Found'
        else:
            return 'Not found'
    
    # recursion
    mid = (left + right) // 2
    if A[mid] == target:
        return 'Found'
    if A[mid] < target:
        return binarysearch(A, target, mid, right)
    if A[mid] > target:
        return binarysearch(A, target, left, mid)
    

print(binarysearch([1,2,3,4,5,6,7,8], 1))