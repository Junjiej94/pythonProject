import math

def isPrime(n):
    for i in range(2, math.ceil(n / 2)+1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    print(isPrime(4))
