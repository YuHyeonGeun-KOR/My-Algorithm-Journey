import sys
input =sys.stdin.readline

n , d = map(int, input().split())
INF  = 1e9

distance = [i for i in range(d+2)]

start = 0
point = []
for _ in range(n):
    start,end,cost = map(int,input().split())
    point.append([start,end,cost])

point = sorted(point,key = lambda x : (x[0],x[1],x[2]))

for i in point:
    start,end,cost = i
    if end<=d:
        distance[end] = min((distance[start] + cost , distance[end]))
    for j in range(start,d+1):
        distance[j] = min(distance[j-1] +1, distance[j])
result = 0

for i in range(1,d+1):
    result = min((result +1) , distance[i])

print(result)
