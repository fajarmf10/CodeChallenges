#!/bin/python3

import sys

def countingValleys(n, s):
    # Complete this function
    count = 0
    current = 0
    for a in s:
        if(a=='U'): current+=1
        if(a=='D'): current-=1
        if(current==0 and a=='U'): count+=1
    return(count)

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)
