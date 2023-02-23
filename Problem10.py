import math


def isPrime(n):
    for i in range(2, math.ceil(n / 2)+1):
        if n % i == 0:
            return False
    return True


def getPrimes(n):
    primes = 0
    x = 2
    while x <= n:
        if isPrime(x):
            primes += x
        x += 1
    return primes


if __name__ == '__main__':
    n = 2000000
    primes = getPrimes(n)
    print(primes)
