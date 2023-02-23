import math


def isPalindrome(n):
    n = str(n)
    for i in range(0, math.ceil(len(n) / 2)):
        if n[i] != n[-1 - i]:
            return False
    return True


if __name__ == '__main__':

    print(isPalindrome(1021))
