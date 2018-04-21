#!/bin/python3

import sys

def migratoryBirds(n, ar):
    # Complete this function
    result = [0]*n
    for a in ar:
        result[a]+=1
    return(result.index(max(result)))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
