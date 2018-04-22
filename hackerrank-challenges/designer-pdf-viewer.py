#!/bin/python3

import sys

def designerPdfViewer(h, word):
    # Complete this function
    word = word.lower()
    lword = list(word)
    maxx = 0
    for char in range(len(lword)):
        lword[char] = ord(lword[char]) - 97
    for i in range(len(lword)):
        if(maxx==0 or maxx<h[lword[i]]):
            maxx = h[lword[i]]
    sum = len(word)*1*maxx
    return sum

if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)
