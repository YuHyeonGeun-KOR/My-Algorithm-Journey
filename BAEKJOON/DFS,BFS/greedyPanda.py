from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())

board = []

for i in range(n):
    board.append(list(map(int , input().split())))

result = 0 
dx = [0,0,-1,1]
dy = [1,-1,0,0]

visited = [[0]* n   for _ in range(n)] 

def count_moving(x,y,visited):
    if visited[x][y] > 0 : 
        return visited[x][y]

    visited[x][y] = 1
    rice = board[x][y] 
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
       
        if 0 <= nx < n and 0 <= ny < n:
            next_rice = board[nx][ny]
            if next_rice > rice:
                visited[x][y] = max(visited[x][y] ,count_moving(nx, ny , visited) + 1)
                
    return visited[x][y]


for i in range(n):
    for j in range(n):
        result = max(result , count_moving(i,j,visited))


print(result) 