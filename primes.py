import itertools
from math import sqrt

def primes():
    x = 2
    yield x
    x += 1
    while True:
        prime = True
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                prime = False
                break
        if prime:
            yield x
        x += 1



print(list(itertools.takewhile(lambda x : x <= 31, primes())))