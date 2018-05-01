#!/bin/python3

import sys

result = []

def sieveofdito(n):
    prime = [True] * (n+1)
    p = 2
    while(p*p<=n):
        if(prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p+=1

    for i in range(2, n+1):
        if(prime[i]):
            result.append(i)


if __name__ == '__main__':
    sieveofdito(104729)
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(result[n-1])