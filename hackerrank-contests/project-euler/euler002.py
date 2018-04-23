#!/bin/python3

import sys

def fiboSumEven(n):
    answer=0
    curr=1
    next=2
    while(curr<=n):
        if(curr%2==0):
            answer+=curr
        curr, next = next, curr+next
    return(answer)


if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(fiboSumEven(n))