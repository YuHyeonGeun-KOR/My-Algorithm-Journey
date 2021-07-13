import sys
from collections import deque
import heapq
input = sys.stdin.readline



n= int(input())

time = []
max_count = 0
for i in range(n):
    c_number,start, end = map(int,input().split())
    heapq.heappush(time,[start,end])
result = 0
count = 0
room =[]


while time:
    data = heapq.heappop(time)
    trigger = True

    if len(room) == 0:
        count += 1
        heapq.heappush(room,[data[1],count])
        continue
  
    i = heapq.heappop(room)

    if i[0] <= data[0]:
        i[0] =data[1]
        heapq.heappush(room,[i[0],count])
        trigger = False
    else:
        heapq.heappush(room,[i[0],count])    


    if trigger == True:
        count +=1
        heapq.heappush(room,[data[1],count])        



print(len(room))