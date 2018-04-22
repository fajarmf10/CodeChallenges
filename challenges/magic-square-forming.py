#!/bin/python3

import sys

def formingMagicSquare(s):
    # Complete this function
    # http://www.dr-mikes-math-games-for-kids.com/3x3-magic-square.html
    magic_3_square = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4],
                      [4, 3, 8, 9, 5, 1, 2, 7, 6], [2, 7, 6, 9, 5, 1, 4, 3, 8],
                      [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5, 7, 8, 1, 6],
                      [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2]]
    result = [0]*8
    for i in range(8):
        for j in range(9):
            result[i] += abs(magic_3_square[i][j] - s[int(j//3)][j%3])
    return(min(result))


if __name__ == "__main__":
    s = []
    for s_i in range(3):
       s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
       s.append(s_t)
    result = formingMagicSquare(s)
    print(result)
