import sys
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def fire_bfs (fire_list,board, x,y):
    fire_x = fire_list[0]
    fire_y = fire_list[1]
    fire_visited = [[0] * y for _ in range(x)]
    fire_queue = deque()
    fire_visited[fire_x][fire_y] = 1

    fire_queue.append([fire_x,fire_y])

    while fire_queue:
        xx , yy = fire_queue.popleft()
        
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0<= nx < x and 0<= ny < y and board[nx][ny] != "#":
                if fire_visited[nx][ny] == 0:
                    fire_visited[nx][ny] = fire_visited[xx][yy] + 1
                    fire_queue.append([nx,ny])
    return fire_visited
                
def sangguen_move(sangguen_positions,visited,board, x,y):
    s_x = sangguen_positions[0]
    s_y = sangguen_positions[1]
    s_visited = visited
    s_queue = deque()
    s_visited[s_x][s_y] = 1

    s_queue.append([s_x,s_y])

    while s_queue:
        xx , yy = s_queue.popleft()
        
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0<= nx < x and 0<= ny < y and board[nx][ny] != "#":
                if s_visited[nx][ny] > s_visited[xx][yy]:
                    s_queue.append([nx,ny])
                    s_visited[nx][ny]  >=  s_visited[xx][yy] + 1
            elif (0 > nx or  nx > x or  0 > ny or ny > y ) and board[xx][yy] != ".":
                return s_visited[xx][yy] + 1
    return False  

n = int(input())

for i in range(n):
    board = []
    y , x = map(int, input().split())

    fire_list = []
    sangguen_positions = []
    for j in range(x):
        board.append(list(input().rstrip()))
    
    for k in range(x):
        for l in range(y):
            if board[k][l] == "*":
                fire_list = [k,l]

            if board[k][l] == "@":
                sangguen_positions = [k,l]

    visited = fire_bfs(fire_list ,board, x,y)
    result = sangguen_move(sangguen_positions,visited, board , x,y) 
    if result == False:
        print("IMPOSSIBLE")
    else:
        print(result)

                
