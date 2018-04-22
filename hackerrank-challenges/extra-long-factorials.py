#!/bin/python3

import sys

def extraLongFactorials(n):
    # Complete this function
    list = [0] * int(n+1)
    if((n==0) or (n==1)):
        return 1
    else:
        if(list[n]!=0):
            return list[n]
        else:
            return((n*extraLongFactorials(n-1)))

if __name__ == "__main__":
    n = int(input().strip())
    print(extraLongFactorials(n))
