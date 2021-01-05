from collections import deque
m,n = map(int, input().split())

Box = [0]*n
for i in range(n):
    Box[i] = list(map(int, input().split()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
for i in range(n):
    for j in range(m):
        if Box[i][j] == 1:
            queue.append((i,j))

def dfs(queue):
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or nx <0 or ny >= m or ny < 0:
                continue

            if Box[nx][ny] == -1: 
                continue
            if Box[nx][ny] == 0:
                Box[nx][ny] = Box[x][y]+1
                queue.append((nx,ny))
          
    
dfs(queue)


def solve(Box):
    for i in range(n):
        if 0 in Box[i]:
            return -1
    r =  max(map(max, Box))
    return r-1


print(solve(Box))