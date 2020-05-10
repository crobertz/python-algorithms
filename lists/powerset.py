from itertools import chain, combinations

def powerset(n):
    """
    Given positive integer n, returns powerset of {0,1,...,n-1}
    """
    # initialize with emptyset
    subsets = [[]]
    
    # contains subsets from previous round
    prev_subsets = []

    # initialize with singletons
    for i in range(n):
        prev_subsets.append([i])
    subsets.extend(prev_subsets)

    # iterate over length of subset
    for length in range(1,n):
        # size k+1 subsets to be added
        new_subsets = []

        # at step k, prev_subsets = subsets of size k
        # for each k-subset, add number ranging from largest element to n-1
        for subset in prev_subsets:
            last = subset[-1]
            for num in range(last+1,n):
                new_subset = subset + [num]
                new_subsets.append(new_subset)
        
        # add newly found subset
        subsets.extend(new_subsets)

        # update new_subsets to be set of all size k+1 subsets
        prev_subsets = new_subsets
    
    return subsets

# using itertools
def powerset_iter(n):
    """returns generator for powerset of {0,1,...,n-1}"""
    # chain r-combinations generator for r=0, 1,..., n
    return chain.from_iterable(combinations(range(n), r) for r in range(n+1))