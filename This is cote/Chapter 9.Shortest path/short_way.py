## 내 코드 
'''
import sys
import heapq
input =sys.stdin.readline

n , d = map(int, input().split())
INF  = 1e9

distance = [i for i in range(d+2)]

start = 0
point = []
for _ in range(n):
    a,b,c = map(int,input().split())
    point.append([a,b,c])

point = sorted(point,key = lambda x : (x[0],x[1],x[2]))

for i in point:
    a,b,c = i
    distance[b] = min((distance[a] + c , distance[b]))
result = 0

for i in range(1,d+1):
    result = min((result +1) , distance[i])

print(result)
'''
## 내 코드와 비슷한 솔루션 풀이 

import sys
import heapq
input =sys.stdin.readline

n , d = map(int, input().split())
INF  = 1e9

distance = [i for i in range(d+2)]

start = 0
point = []
for _ in range(n):
    a,b,c = map(int,input().split())
    point.append([a,b,c])

point = sorted(point,key = lambda x : (x[0],x[1],x[2]))

for i in point:
    a,b,c = i
    if b<=d:
        distance[b] = min((distance[a] + c , distance[b]))
    for j in range(a,d+1):
        distance[j] = min(distance[j-1] +1, distance[j])
result = 0

for i in range(1,d+1):
    result = min((result +1) , distance[i])

print(result)

## 지름길 값 초기화하고 그 구간부터 뒷부분을 미리 바꿔주기만 하면 됐다 