import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
wall_count = [[1e9]* n  for _ in range(m)] 
for i in range(m):
    board.append(list(map(int, input().rstrip())))

wall_count[0][0] = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

queue = deque()
queue.append((0,0))

while queue:
    x ,y = queue.popleft()

    for i in range(4):
        xx = dx[i] + x
        yy = dy[i] + y

        if 0<= xx < m  and 0<= yy < n :
            if board[xx][yy] == 1  :
                cost = wall_count[x][y] + 1
                if cost < wall_count[xx][yy]:
                    wall_count[xx][yy] = cost
                    queue.append((xx,yy))
            elif board[xx][yy] == 0:
                if wall_count[x][y] <  wall_count[xx][yy]:
                    wall_count[xx][yy] = wall_count[x][y]
                    queue.append((xx,yy))

print(wall_count[-1][-1])
    
 
