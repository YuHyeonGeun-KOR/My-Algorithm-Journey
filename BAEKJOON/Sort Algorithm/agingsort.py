import sys
input = sys.stdin.readline

array = []

n = int(input())

for i in range(n):
    array.append([i,list(input().rstrip().split())])

array = sorted(array, key = lambda x:(int(x[1][0]) , x[0]))


for i in array:
    print(i[1][0],i[1][1])