from collections import deque

m,n,h= map(int, input().split())
Box = [[] for i in range(h)]
for i in range(h):
    for j in range(n):
        Box[i].append(list(map(int, input().split())))
#Box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if Box[i][j][k] == 1:
                queue.append((i,j,k))


def dfs():
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nh = z + dh[i]
            #if 0 <= nx < n and 0 <= ny < m and 0 <= nh <h and Box[nh][nx][ny] == 0 and visit[nh][nx][ny] == 0:
            if 0 <= nx < n and 0 <= ny < m and 0 <= nh < h and Box[nh][nx][ny] == 0:
                Box[nh][nx][ny] = Box[z][x][y]+1
                queue.append((nh,nx,ny))
            
            
            
dfs()


            
def solve(Box):
    temp = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if Box[i][j][k] == 0:
                    return -1
                temp = max(temp, Box[i][j][k])
    return temp-1

print(solve(Box))