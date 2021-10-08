import sys
import heapq
input = sys.stdin.readline

v , e = map(int, input().split())

start = int(input())

INF = sys.maxsize
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1) 



for i in range(e):
    left , right , c = map(int, input().split())

    graph[left].append((right ,c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] =0

    while q:
        dist , now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])