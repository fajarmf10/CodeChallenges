#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    # Complete this function
    result = 0
    for a in range(len(ar)-1):
        for b in range(a+1, len(ar)):
            if((ar[a]+ar[b])%k == 0):
                result+=1
    return result

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
