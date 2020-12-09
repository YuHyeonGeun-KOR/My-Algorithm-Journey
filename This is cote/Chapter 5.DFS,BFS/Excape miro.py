from collections import deque
N,M = map(int,input().split())

graph = [[int(x) for x in input()] for _ in range(N)]


dx = [-1, +1, 0 ,0]
dy = [0, 0, -1, +1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()

        for i in range (4):
            xx = x + dx[i]
            yy = y + dy[i]

            if xx <= -1 or xx >= N or yy <= -1 or yy >= M:
                continue 
            elif graph[xx][yy]==1:
                graph[xx][yy] = graph[x][y] + 1
                queue.append((xx,yy))
            elif graph[xx][yy]==0:
                continue
    return graph[N-1][M-1]            

print(bfs(0,0))











