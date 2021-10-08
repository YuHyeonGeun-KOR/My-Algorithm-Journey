import sys
import heapq
input = sys.stdin.readline

n = int(input())

distance = [1e9]* (n+1)

graph = [[] for i in range(n+1)]

m = int(input())

for i in range(m):
    left , right , cost = map(int, input().split())

    graph[left].append((right, cost))

def dsktra(start):
    q = [(0,start)]

    distance[start] = 0

    while q:
        cost , now = heapq.heappop(q)

        if distance[now] < cost:
            continue

        for i in graph[now]:
            next_cost = cost  + i[1]

            if next_cost < distance[i[0]] :
                distance[i[0]] = next_cost
                heapq.heappush(q,(next_cost,i[0]))

start , end = map(int, input().split())

dsktra(start)
print(distance[end])