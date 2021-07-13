import sys
import heapq
from collections import deque 
input = sys.stdin.readline

n = int(input())

array = []
for i in range(n):
    name , score = input().split()
    
    heapq.heappush(array,(score,name))

for i in array:
    print(i[1] ,  end = " ")

