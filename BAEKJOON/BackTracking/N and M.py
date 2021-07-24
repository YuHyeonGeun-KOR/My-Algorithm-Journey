from itertools import permutations
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
array = []
for i in range(1,n+1):
    array.append(i)
array = permutations(array,m)
for i in array:
    for j in range(m):
        print(i[j] , end=" ")
    print("")

