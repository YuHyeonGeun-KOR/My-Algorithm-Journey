from collections import deque

n,m = map(int, input().split())

Miro = [0]*n

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    Miro[i] = list(map(int, input()))

def bfs (x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if Miro[ny][nx] == 0:
                continue

            if Miro[ny][nx] == 1:
                Miro[ny][nx] = Miro[y][x] + 1
                queue.append((nx,ny))

    return Miro[n-1][m-1] 

print(bfs(0,0))