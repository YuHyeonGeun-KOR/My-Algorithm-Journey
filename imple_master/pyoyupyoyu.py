import sys
from collections import deque
input = sys.stdin.readline

visited = [[False] * 6 for _ in range(12)]

board = []
for i in range(12):
    board.append(list(input().rstrip()))

def counting(color,x,y):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    m_cnt = 1
    queue = deque()
    position = []
    position.append([x,y])
    queue.append([1,x,y])
    visited[x][y] = True
    
    while queue:
        cnt ,nx, ny = queue.popleft()
        for i in range(4):
            xx = nx + dx[i]
            yy = ny + dy[i]

            if 0 <= xx < 12 and 0 <= yy <6 and board[xx][yy] == color and visited[xx][yy] == False:
                visited[xx][yy]  = True
                m_cnt += 1
                queue.append([cnt,xx,yy])
                position.append([xx, yy])
    return m_cnt, position

def down(y):
    queue = deque()
    
    for j in range(12):
        if board[j][y] == ".":
            queue.append(board[j][y])
        else:
            queue.appendleft(board[j][y])

        
    for j in range(12):
        board[j][y] = queue.pop()

   
result  = 0 

while True:
    
    continue_flag = False
   
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and visited[i][j] == False:
                max_count , del_list = counting(board[i][j],i,j)

                if max_count >= 4:
                    continue_flag = True
                    for d in del_list:
                        board[d[0]][d[1]] = '.'

    if continue_flag:
        result += 1
        for i in range(6):
            down(i)
            visited = [[False] * 6 for _ in range(12)]
       

    if not continue_flag:
        break

    
print(result)