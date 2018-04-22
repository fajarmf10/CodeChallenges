#!/bin/python3

import sys

def solve(s, d, m):
    # Complete this function
    count = 0
    for piece in range(0, len(s)+1-m):
        if sum(s[piece : piece + m]) == d:
            count += 1
    return count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(s, d, m)
print(result)
