#!/bin/python3

import os
import sys

#
# Complete the climbingLeaderboard function below.
#
def climbingLeaderboard(scores, alice):
    #
    # Write your code here.
    #
    leaderboard = [0] * (len(scores)+1)
    for i in range(0, len(scores)):
        if (i==0):
            leaderboard[i+1]=1
        else:
            leaderboard[i] = leaderboard[i-1]
            if(scores[i]<scores[i-1]):
                leaderboard[i] = leaderboard[i]+1

    counterB = len(scores)-1
    for i in range(0, len(alice)):
        x = alice[i]
        answ=0
        while(counterB>0 and x>scores[counterB]):
            counterB-=1

        if(x==scores[counterB]):
            answ = leaderboard[counterB]
        elif(x<scores[counterB]):
            answ = leaderboard[counterB]+1
        print(answ+1)


if __name__ == '__main__':
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(scores, alice)