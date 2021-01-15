from collections import deque

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]

visited = [False]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[a].sort()

result = 0

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start]= True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]= True
    return visited
            
 

bfs(graph,1,visited)

for i in range(1,n+1):
    if visited[i] == True:
        result += 1
        
print(result-1)