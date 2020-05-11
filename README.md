# python-algorithms

Various algorithms implemented in python.

### numbertheory
Number theoretic algorithms.

#### `erasieve`
Sieve of Eratosthenes for finding prime numbers below a given integer.

#### `factors`
`factors(n)` returns the set of factors of `n`.
`prime_factors(n)` returns the set of prime factors of `n`.

### murnaghan-nakayama
Recursive Murnaghan-Nakayama rule for computing irreducible character values of symmetric groups.

### lists
Algorithms using lists.

#### `cumulative_sum`
Given a list of numbers returns a list of cumulative sums.

#### `powerset`
Given an integer `n` returns a list of subsets of {0,1,...,n-1}.

#### `sort`
Basic sorting algorithms.
`insertionsort`
`bubblesort`

#### `heap`
Heap algorithms.
`parent`, `left_child`, `right_child`
Given a heap implemented as a list return respective indices.
`max_heapify`
Assuming trees at children of given node are max heaps turn tree rooted at given node into max heaps.
`build_max_heap`
Given a list of numbers return a max heap structure.
`heapsort`
Returns a sorted copy of a list of numbers (not in-place).
