import math

def getFactors(n):
    factors = []
    x = 2
    while x <= n:
        if n%x == 0:
            factors.append(x)
            n = n/x
            x = 2
        else:
            x += 1

    return factors

def isDivisible(x,i):
    if x % i == 0:
        return True
    else:
        return False


def multiply(factors, x):
    multi = []
    k = x
    for i in factors:
        if k % i != 0:
            multi.append(i)
        if k % i == 0:
            k = k/i
    for i in multi:
        x = x * i
    return x


if __name__ == '__main__':
    pepe = 18
    x = 1
    for i in range(1, pepe):
        if not isDivisible(x, i):
            factors = getFactors(i)
            x = multiply(factors, x)
    print(x)
