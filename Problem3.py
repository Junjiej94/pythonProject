def isPrime(n):
    for i in range(2, math.ceil(n / 2)):
        if n % i == 0:
            return False
    return True


import math

if __name__ == '__main__':
    list = []
    n = 600851475143
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            if isPrime(i):
                list.append(i)

    print(list[-1])
    print(list)
