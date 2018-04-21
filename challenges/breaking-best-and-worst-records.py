#!/bin/python3

import os
import sys

#
# Complete the breakingRecords function below.
#
def breakingRecords(scores):
    #
    # Write your code here.
    #
    minScore, maxScore = 0, 0
    bh, bl = 0, 0
    index = 0
    for score in scores:
        if(index==0):
            minScore = score
            maxScore = score
        else:
            if (score<minScore):
                bl+=1
                minScore = score
            else:
                if (score > maxScore):
                    bh+=1
                    maxScore = score
        index+=1
    return [bh, bl]

if __name__ == '__main__':
    n = int(input())
    score = list(map(int, input().split()))
    result = print(*breakingRecords(score))