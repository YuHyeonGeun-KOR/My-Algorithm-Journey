import sys

input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

N,M = map(int, input().split())

x,y,d = map(int, input().split())

board =[]
for i in range(N):
    board.append(list(map(int, input().split())))

count = 0
turn_count = 0

while (True):
    d -=1
    if d < 0:
        d = 3

    if board [ x + dx[d] ][ y + dy[d] ] == 0:
        x += dx[d] 
        y += dy[d]
        board[x][y] = 1
        count += 1
        turn_count = 0
    elif board [ x + dx[d] ][ y + dy[d] ] == 1:
        turn_count +=1
    
    if turn_count == 4:
        d -=1
        if d < 0:
            d = 3
        if board [ x + dx[d] ][ y + dy[d] ] == 0:
           x += dx[d] 
           y += dy[d]
           board[x][y] = 1
           count += 1
           turn_count = 0
        elif board [ x + dx[d] ][ y + dy[d] ] == 1:
            break

print(count)