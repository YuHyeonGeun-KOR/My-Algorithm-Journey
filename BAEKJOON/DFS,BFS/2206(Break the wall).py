from collections import deque
from copy import deepcopy   
import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())

Miro = []
visit = [[[0]*2 for i in range(m)] for i in range(n)]
visit[0][0][1] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    Miro.append(list(map(int, list(input().strip()))))

def bfs ():
    queue = deque()
    queue.append((0,0,1))
    
    while queue:
        
        x,y,cn = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visit[x][y][cn]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or nx <0 or ny >= m or ny < 0:
                continue
            
            if Miro[nx][ny] == 1 and cn == 1:
                visit[nx][ny][0] = visit[x][y][1] + 1
                queue.append((nx,ny,0))        
            elif Miro[nx][ny] == 0 and visit[nx][ny][cn] == 0:
                    visit[nx][ny][cn] = visit[x][y][cn] + 1
                    queue.append((nx,ny,cn))
            
    return -1


print(bfs())