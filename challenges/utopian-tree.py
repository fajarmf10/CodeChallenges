#!/bin/python3

import sys

def utopianTree(n):
    # Complete this function
    height = 1
    if(n==0):
        return 1
    for i in range(n):
        if(i%2==0):
            height*=2
        else:
            height+=1
    return(height)

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = utopianTree(n)
        print(result)
