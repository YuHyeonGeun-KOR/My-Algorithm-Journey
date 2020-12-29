import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split())
INF = int(1e9)

start = int(input())

distance =  [INF]*(n+1)


graph = [[] for _ in range(1,n+1)]

for _ in range(m):
    a,b,c = map(int , input().split())
    graph[a].append((b,c))

def dijkstra (start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now]<dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

