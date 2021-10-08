import sys
import heapq
input = sys.stdin.readline

n , m = map(int, input().split())



graph = [[] for i in range(n+1)]


for i in range(m):
    left , right , cost = map(int, input().split())

    graph[left].append((right, cost))
    graph[right].append((left, cost))
def dsktra(start ,end):
    q = [(0,start)]
    distance = [1e9]* (n+1)
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
    return distance[end]

mid1 , mid2 = map(int, input().split())

p1 = dsktra(1,mid1) + dsktra(mid1 , mid2)  + dsktra(mid2 , n)
p2 = dsktra(1,mid2) + dsktra(mid2 , mid1)  + dsktra(mid1 , n)

if p1 >= 1e9 and p2 >= 1e9:
    print(-1)
else:
    print(min(p1,p2))