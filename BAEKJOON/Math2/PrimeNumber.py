import math
import sys 
input = sys.stdin.readline

n= int(input())
checkList = list(map(int, input().split()))

prime = [True] * 1001

m = int(1001 ** 0.5)

prime[1] =False

for i in range(2,m+1):
    if prime[i] == True:    
        for j in range(i+i,1001, i):
            prime[j] = False

count = 0
for i in checkList:
    if prime[i] == True:
        count+=1

print(count) 
