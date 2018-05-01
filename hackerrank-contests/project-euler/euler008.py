#!/bin/python3

import sys

def biggestproduct(num, k):
    result = max(intprod(num[i: i + k]) for i in range(len(num) - k + 1))
    return(result)


def intprod(string):
    result = 1
    for char in string:
        result *= int(char)
    return(result)


if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n,k = input().strip().split(' ')
        n,k = [int(n),int(k)]
        num = input().strip()
        print(biggestproduct(num, k))
