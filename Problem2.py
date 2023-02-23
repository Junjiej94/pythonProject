if __name__ == '__main__':
    fib = [1]
    n = 1
    k = 2
    sum = 0
    while k <= 4000000:
        fib.append(k)
        p = k
        k += n
        n = p
    for x in fib:
        if x % 2 == 0:
            sum += x
    print(sum)

