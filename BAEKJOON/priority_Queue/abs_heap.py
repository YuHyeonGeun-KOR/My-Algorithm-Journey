import heapq
import sys

input = sys.stdin.readline
queue = []

n = int(input())
result = []
for i in range(n):
    x = int(input())
    x_arr = []

    if x < 0:
        x_arr = [abs(x),-1]
        heapq.heappush(queue,x_arr)
    elif x > 0:
        x_arr = [x,1]
        heapq.heappush(queue,x_arr)
    else :
        if len(queue) == 0:
            result.append(0)
        else:
            temp = heapq.heappop(queue)
            result.append((temp[0] * temp[1]))
        
for i in result :
    print(i)