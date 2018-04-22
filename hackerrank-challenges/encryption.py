#!/bin/python3

import sys
from math import sqrt, floor, ceil

def encryption(s):
    # Complete this function
    length = len(s)
    row = int(floor(sqrt(length)))
    column = int(ceil(sqrt(length)))
    if((row*column) < length):
        row+=1
    result = [[0 for _ in range(column)] for __ in range(row)]
    it, i, j = [0,0,0]
    while(it < length):
        result[i][j] = s[it]
        it+=1
        j+=1
        if(j==column):
            j=0
            i+=1
    output = ""
    for i in range(column):
        for j in range(row):
            if(result[j][i] !=0):
                output += result[j][i]
        output += " "
    return(output)

if __name__ == "__main__":
    s = input().strip()
    result = encryption(s)
    print(result)
