import heapq
import sys

input = sys.stdin.readline
queue = []

n = int(input())
result = []
for i in range(n):
    x = int(input())
    x = x*-1
    if  x== 0:
        if len(queue) == 0:
            result.append(0)
        else:
            result.append(-1 * heapq.heappop(queue))
    else:
        
        heapq.heappush(queue,x)
for i in result :
    print(i)
