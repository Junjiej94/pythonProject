import math

def isPrime(n):
    for i in range(2, math.ceil(n / 2)+1):
        if n % i == 0:
            return False
    return True


def getPrimes(n):
    primes = []
    x = 2
    while len(primes) <= n:
        if isPrime(x):
            primes.append(x)
        x += 1
    return primes


if __name__ == '__main__':
    n = 10001
    primes = getPrimes(n)
    print(primes[10001-1])

