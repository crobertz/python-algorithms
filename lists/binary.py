def binarysearch(A, target, left=0, right=None):
    """Searches A for target and returns 'Found' if found and 'Not found' otherwise"""
    
    # base cases
    if not A:
        return 'Not found'
    if right == None:
        right = len(A)-1
    if left == right:
        if A[left] == target:
            return 'Found {} at index {}'.format(target, left)
        else:
            return 'Not found'
    
    # recursion
    mid = (left + right) // 2

    if A[mid] == target:
        return 'Found {} at index {}'.format(target, mid)
    if A[mid] < target:
        return binarysearch(A, target, mid+1, right)
    if A[mid] > target:
        return binarysearch(A, target, left, mid-1)
    

for i in range(10):
    print(binarysearch([1,2,3,4,5,6,7,8], i))