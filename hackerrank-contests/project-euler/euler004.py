#!/bin/python3

import sys

palindrome = []


def checkPalindrome(n):
    stN = str(n)
    return(stN==str(n)[::-1])


def getPalindrome():
    for i in range(100, 1000):
        for j in range(100, 1000):
            prod = i*j
            if(checkPalindrome(prod) and prod not in palindrome):
                palindrome.append(prod)
    palindrome.sort()


def searchList(n):
    for _ in range(len(palindrome)-1, -1, -1):
        if(palindrome[_] < n):
            return(palindrome[_])


if __name__ == '__main__':
    getPalindrome()
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(searchList(n))
