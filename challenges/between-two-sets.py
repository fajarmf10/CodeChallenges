#!/bin/python3

import os
import sys

def lcm(a, b):
    return((a/gcd(a, b))*b)


def gcd(a, b):
    while(a and b):
        if(a>=b):
            a%=b
        else:
            b%=a
    return(a+b)


#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #
    multiple = 0
    for i in b:
        multiple = gcd(multiple, i)
    factor = 1
    for i in a:
        factor = lcm(factor, i)
        if(factor > multiple):
            return 0
    if(multiple % factor != 0):
        return 0

    value = multiple/factor

    maxx = max(factor, value)
    totalX = 1

    for i in range(int(factor), int(multiple-1)):
        if(multiple % i == 0 and i % factor == 0):
            totalX+=1

    return totalX

if __name__ == '__main__':
    nm = input().strip().split(' ')
    n = int(nm[0])
    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)
    print(total)