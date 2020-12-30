from collections import deque


n,m,start = map(int, input().split())


def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start]= True
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]= True

graph = [[] for i in range(n+1)]

visited = [False]*(n+1)
visited1 = [False]*(n+1)
for i in range(0,m):
    a,b = map(int, input().split())
    graph[a].append(b)

print(graph)
dfs(graph,start,visited) 
print('')
print(graph)
bfs(graph,start,visited1)   