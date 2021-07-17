
import sys
from collections import deque

input = sys.stdin.readline


N,M,K,X = map(int, input().split())

road = [[] for _ in range(N+1)]
for i in range(M):
    left , right = map(int, input().split())
    road[left].append(right)

visited = [False] * (N+1)
distance = [0]*(N+1)

def bfs (start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while (queue):
        starting_city = queue.popleft()
        
        for i in road[starting_city]:
            if visited[i] ==False:
                visited[i] =True
                distance[i] = distance[starting_city] + 1 
                queue.append(i)
       
               
bfs(X)
result = []


for i in range(len(visited)):
    if distance[i] == K:
        result.append(i)

result = sorted(result)
if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)