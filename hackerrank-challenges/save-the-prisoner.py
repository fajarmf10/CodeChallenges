#!/bin/python3

import sys

def saveThePrisoner(n, m, s):
    # Complete this function
    m%=n
    result=(m+s-1)%n
    if (result==0):
        result=n
    return(result)


t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
