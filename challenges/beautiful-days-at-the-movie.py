#!/bin/python3

import sys

def beautifulDays(i, j, k):
    count=0
    for a in range(i, j+1):
        if ((a - int(str(a)[::-1])) % k == 0):
            count+=1
    return(count)
    # Complete this function

if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print(result)
