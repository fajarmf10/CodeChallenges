#!/bin/python3

import sys

def viralAdvertising(n):
    # Complete this function
    shared=5
    total=0
    for _ in range(0, n):
        opened = int(shared/2)
        total=total+opened
        shared=opened*3
    return(total)

if __name__ == "__main__":
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)
