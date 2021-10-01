from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
result = []

def bfs(x,y,end_x,end_y):
    
    queue = deque()
    queue.append((x,y))
    table[x][y] = 1
    while queue:
        c_x,c_y = queue.popleft()
        if  c_x == end_x and c_y == end_y :
            result.append(table[end_x][end_y] -1)
            return
        for i in range(8):
            e_x = c_x + dx[i]
            e_y = c_y + dy[i]

            if 0 <= e_x < l and 0 <= e_y < l and table[e_x][e_y] == 0:
                table[e_x][e_y] = table[c_x][c_y] + 1
                queue.append((e_x,e_y))
            
                
for i in range(n):
    l = int(input())
    start_x,start_y = map(int, input().split())
    end_x ,end_y = map(int, input().split())
    table = [[0]*l for i in range(l)]
    bfs(start_x,start_y,end_x,end_y)


for i in result:
    print(i)
