#!/bin/python3

import sys


def sumsquare(n):
    return(n*(n+1)*(2*n+1)//6)


def squaresum(n):
    return(sum(i for i in range(1, n+1))**2)


def domath(n):
    ans = abs(squaresum(n)-sumsquare(n))
    return ans


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(domath(n))