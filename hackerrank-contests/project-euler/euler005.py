#!/bin/python3

import sys
from math import gcd

def smallestMultiple(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i // gcd(i, ans)
    return(ans)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(smallestMultiple(n))