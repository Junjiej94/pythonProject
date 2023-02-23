def getFactors(n):
    x = 2
    factors = []
    while x <= n:
        if n%x == 0:
            factors.append(x)
            n = n/x
            x = 2
        else:
            x += 1

    return factors


if __name__ == '__main__':
    print(getFactors(69))