import functools
import itertools

def factors(n): 
    # https://stackoverflow.com/a/6800214
    # for i up to sqrt(n) + 1, if i divides n then i and n//i are factors of n
    """Find factors of n"""
    return set(functools.reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def prime_factors(n):
    # https://codereview.stackexchange.com/a/121869
    # i ranges over 2 and odd numbers 3, 5, 7, ...
    # returns each prime as many times as it divides n
    """Find prime factorization of n"""
    for i in itertools.chain([2], itertools.count(3, 2)):
        if n <= 1:
            break
        while n % i == 0:
            n //= i
            yield i