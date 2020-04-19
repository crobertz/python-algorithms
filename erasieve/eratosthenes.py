#sieve of eratosthenes for finding primes less than n

import sys

def eratosthenes(n):
    """list all primes less than n"""
    #set of all numbers between 2 and n to be sieved
    primes = set(range(2,n))

    #for each i in range(2,n) delete all larger multiples of i in primes set
    #start check at i**2 since any less will be deleted by previous prime
    for i in range(2,n):
        if i in primes:
            j = i**2
            while j < n:
                if j in primes:
                    primes.remove(j)
                j += i

    return(primes)

def main():
    n = int(sys.argv[1])
    primes = eratosthenes(n)
    print("number of primes less than %d:" % n)
    print(primes)
    print("total: " + str(len(primes)))


if __name__ == "__main__":
    main()
