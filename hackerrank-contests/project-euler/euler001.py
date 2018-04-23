#!/bin/python3

import sys

def factor_of_n(k, n):
    m = (k-1)//n
    return(n*m*(m+1)//2)


def compute(n):
    return(factor_of_n(n, 3) + factor_of_n(n, 5) - factor_of_n(n, 15))


if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(compute(n))