#!/bin/python3

import sys

def pickingNumbers(arr):
    # Complete this function
    maxInt = 0
    for i in arr:
        a=arr.count(i)
        b=arr.count(i-1)
        a+=b
        if(a>maxInt):
            maxInt=a
    return(maxInt)

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = pickingNumbers(a)
    print(result)
