from itertools import combinations
import sys
input = sys.stdin.readline
n= int(input())
arr_c =[]
check = []
arr = list(map(int, input().split()))


for k in range(1,n+1):
    for i in combinations(arr,k):
        if sum(i) not in check:
            check.append(sum(i))
   
check.sort()

for i in range(1,len(check)):
    if check[i] - check [i-1] > 1:
        print(check[i-1]+1)
        break
