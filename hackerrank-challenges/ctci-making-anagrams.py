from collections import Counter

def number_needed(a, b):
    a = Counter(a)
    b = Counter(b)
    a.subtract(b)
    return(sum(abs(i) for i in a.values()))

a = input().strip()
b = input().strip()
print(number_needed(a, b))
