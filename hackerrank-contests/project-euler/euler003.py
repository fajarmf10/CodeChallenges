#!/bin/python3

import sys
from math import sqrt

def primeFac(n):
    primefactors = []
    i = 2
    if(n==2):
        return(2)
    else:
        while(i*i<=n):
            while(n%i==0):
                primefactors.append(i)
                n//=i
            i+=1
        if(n>1):
            primefactors.append(n)
        return primefactors


if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(max(primeFac(n)))
