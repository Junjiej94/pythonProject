def square_of_sums(x, n):
    sum = 0
    for i in range(n, x+1):
        sum += i
    return sum**2


def sum_of_squares(x, n):
    sum = 0
    for i in range(n, x+1):
        sum += i**2
    return sum


if __name__ == '__main__':
    x = 100
    n = 0
    print(abs(sum_of_squares(x,n) - square_of_sums(x, n)))
