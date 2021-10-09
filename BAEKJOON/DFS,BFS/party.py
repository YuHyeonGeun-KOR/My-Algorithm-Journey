import sys
import heapq
input = sys.stdin.readline

n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    left , right, cost = map(int, input().split())
    graph[left].append([cost, right])


def dsk(start, end):
    visited = [1e9] * (n+1)
    queue = []
    visited[start] = 0
    queue.append([0 , start])

    while queue:
        dist , now = heapq.heappop(queue)

        if visited[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[0]
            if cost < visited[i[1]]:
                visited[i[1]] = cost
                heapq.heappush(queue,[cost , i[1]]) 

    return visited[end]

result = []

for i in range(1, n+1):
    result.append(dsk(i ,x ) + dsk(x, i) )
print(max(result))