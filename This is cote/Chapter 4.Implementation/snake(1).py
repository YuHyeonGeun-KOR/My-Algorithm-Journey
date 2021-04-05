n=int(input())
k=int(input())

board=[[0]*(n+1) for _ in range(n+1)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for _ in range(k):
    apple_x,apple_y = map(int,input().split())
    board[apple_y][apple_x] = 1

l = int(input())

turn = []
for _ in range(l):
    turn_time , turn_direc = input().split()
    turn.append((turn_time,turn_direc))
board[1][1] = 's'

direct = 0
time_count = 0

snake_x = 1
snake_y = 1

position = [(1,1)]


while True:
    nx = snake_x + dx[direct]
    ny = snake_y + dy[direct]

    if 1<= nx <=n and 1<= ny <= n and board[nx][ny] != 's':
        if board[nx][ny] == 0 :
            board[nx][ny] = 's'
            position.append((nx,ny))
            del_x, del_y = position.pop(0)
            board[del_x][del_y] = 0
       
       
        if board[nx][ny] == 1:
            board[nx][ny] = 's'
            position.append((nx,ny))
    
    else:
        time_count += 1
        break

    snake_x = nx
    snake_y = ny
    time_count += 1
    
    if len(turn) != 0 and time_count == int(turn[0][0]):
        if turn[0][1] == 'L':
            direct = (direct - 1) % 4
        elif turn[0][1] == 'D':
            direct = (direct + 1) % 4
        del turn[0]

print(time_count)    
    
            




