#!/bin/python3

import sys

def appendAndDelete(s, t, k):
    # Complete this function
    samechar = min(len(s), len(t))
    for i in range(len(t)):
        if s[:i] != t[:i]:
            samechar = i - 1
            break

    diff = len(s) - samechar + len(t) - samechar
    if((diff<=k) and ((diff%2) == (k%2)) or (len(s)+len(t)<k)):
        return('Yes')
    else:
        return('No')


if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)
