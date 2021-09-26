import heapq
import sys

input = sys.stdin.readline

n= int(input())

time_table = []
for i in range(n):
    time_table.append(list(map(int,input().split())))

time_table = sorted(time_table, key = lambda x :x[0])

q = []
heapq.heappush(q,time_table[0][1])

for i in range(1,n):
    if q[0] > time_table[i][0]:
        heapq.heappush(q,time_table[i][1])

    else:
        heapq.heappop(q)
        heapq.heappush(q,time_table[i][1])

print(len(q)) 