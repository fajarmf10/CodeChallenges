#!/bin/python3

import os
import sys

#
# Complete the countApplesAndOranges function below.
#
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #
    # Write your code here.
    #
    larry, rob = [0, 0]
    for apple in apples:
        if(t>=(a+apple)>=s):
            larry+=1
    for orange in oranges:
        if(t>=(b+orange)>=s):
            rob+=1
    print('{}\n{}'.format(larry, rob))

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])

    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])

    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    apple = list(map(int, input().rstrip().split()))
    orange = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apple, orange)
