#!/bin/python3

import sys

def solve(year):
    # Complete this function
    februari = 0
    if(year==1918):
        februari=28-13
    elif(year<1918):
        if(year%4==0):
            februari=29
        else:
            februari=28
    else:
        if(((year%4==0) and (year%100 != 0)) or (year%400==0)):
            februari=29
        else:
            februari=28
    day=256 - 31 - februari - 31 - 30 - 31 - 30 - 31 - 31
    return("{}.09.{}".format(day, year))


year = int(input().strip())
result = solve(year)
print(result)
