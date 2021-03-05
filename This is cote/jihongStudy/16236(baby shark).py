from collections import deque
import sys
input = sys.stdin.readline
n= int(input())

dx = [-1, +1, 0 ,0]
dy = [0, 0, -1, +1]
x,y = 0 ,0
fish= []
visited =[False]*(n+1)
board = [] 
fish_distance = 0
startfish = []


for i in range(n):
    board.append(list(map(int,input().split())))

timer = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            x,y= i,j
            board[i][j] = 0
        if board[i][j] == 1:
            fish.append([i,j])
        


for f_x,f_y in fish:
    d = abs(f_x-x)+abs(f_y-y)
    if fish_distance == 0 :
        fish_distance = d
        startfish = [f_x,f_y]
    elif d <= fish_distance:
        fish_distance = d
        startfish = [f_x,f_y]

print(x,y)
print(fish)
print(startfish)
print(board)

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited = [[False] * n for _ in range(n)]
   
    tiktok = 0
    shark_size = 2
    sizeup_cnt = 0
    while queue:
        end_checker = True
        for i in range(n):
            for j in range(n):
                if board[i][j] != 0 and board[i][j] < shark_size:
                    end_checker = False
                    break
        if end_checker == True:
            break
        x,y=queue.popleft()
        tiktok += 1
        for i in range (4):
            xx = x + dx[i]
            yy = y + dy[i]

            if xx <= -1 or xx >= n or yy <= -1 or yy >= n:
                continue 
            elif board[xx][yy] != 0 and board[xx][yy]<shark_size:
                board[xx][yy] = 0
                timer[xx][yy] = tiktok
                sizeup_cnt +=1
                if sizeup_cnt == shark_size:
                    sizeup_cnt = 0
                    shark_size += 1
                queue.append((xx,yy))
            elif board[xx][yy]==shark_size or board[xx][yy] == 0:
                timer[xx][yy] = tiktok
                queue.append((xx,yy))
            else:
                continue
        for i in range(n):
            print(timer[i])

        print(" ")
        

bfs(x,y)
max_num = 0
for i in timer:
    if max(i)>=max_num:
        max_num =max(i)

print(max_num)