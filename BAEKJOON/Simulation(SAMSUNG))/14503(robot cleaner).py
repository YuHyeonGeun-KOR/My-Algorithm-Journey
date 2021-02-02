n,m = map(int, input().split())

d = [[0] *m for i in range(n)]

x,y,direct = map(int, input().split())
d[x][y] = 1

array= []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direct
    direct -= 1
    if direct == -1:
        direct = 3

count = 1
time = 0
while (1):
    turn_left()
    nx = x + dx[direct]
    ny = y + dy[direct]

    if d[nx][ny] == 0 and array [nx][ny] == 0:
        d[nx][ny]=1
        x = nx
        y = ny
        count +=1
        time = 0
        continue
    else:
        time += 1

    if time == 4:
        nx = x- dx[direct]
        ny = y - dy[direct]
        if array[nx][ny]==0:
            x = nx
            y = ny
        else:
            break
        time =0
print(count)