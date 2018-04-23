#!/bin/python3

import sys

def hurdleRace(k, height):
    # Complete this function
    maximum = max(height)
    if(k<maximum):
        doses = maximum-k
    else:
        doses=0
    return(doses)

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = list(map(int, input().strip().split(' ')))
    result = hurdleRace(k, height)
    print(result)
