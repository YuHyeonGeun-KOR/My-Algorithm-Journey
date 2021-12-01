import sys
input = sys.stdin.readline


h,w,l = map(int, input().split())

board = []
for i in range(h):
    board.append(list(input().rstrip()))

answer = list(input().rstrip())

dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]

visited = [[[-1] * w for _ in range(h)] for _ in range(101)]
result = 0
def find(i,j,idx):
    global result
    if idx == len(answer)-1:
        visited[idx][i][j] = 1  
        return
    checker = 0 
    for d in range(8):
        xx = i+dx[d]
        yy = j+dy[d]

        if 0<= xx < h and 0<= yy < w: 
            if board[xx][yy] == answer[idx+1] and visited[idx+1][xx][yy] == -1:
                find(xx , yy  ,idx + 1)
            checker += visited[idx+1][xx][yy]
    visited[idx][i][j] = checker


for i in range(h):
    for j in range(w):
        if board[i][j] == answer[0]:
            find(i,j,0)    
            result += visited[0][i][j];        
print(result)
