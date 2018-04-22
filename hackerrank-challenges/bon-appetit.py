n, k = map(int, input().strip().split(' '))
i = [int(x) for x in input().strip().split(' ')]
b = int(input().strip())

if((sum(i) - i[k])/2 == b):
    print("Bon Appetit")
else:
    print(int(i[k]/2))