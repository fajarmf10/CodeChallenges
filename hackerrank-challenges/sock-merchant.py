#!/bin/python3

import sys
from collections import Counter

def sockMerchant(n, ar):
    # Complete this function
    pairs = 0
    socks = Counter(ar)
    for sock in socks:
        pairs+=socks[sock]//2
    return(pairs)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
