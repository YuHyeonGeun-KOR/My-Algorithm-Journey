import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]

result = []
idx = 1
while True:
    n= int(input())
    if n == 0 :
        break

    board = []
    distance = [[1e9] * n for _ in range(n)]
    for i in range(n):
        board.append(list(map(int, input().split())))

    distance[0][0] = board[0][0]

    queue = deque()
    queue.append([0,0])
    while queue:
        x , y = queue.popleft()

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0<= xx < n and  0<= yy < n:
                cost = board[xx][yy] + distance[x][y]
                if cost < distance[xx][yy]:
                    distance[xx][yy] = cost
                    queue.append([xx,yy])

    result.append(distance[-1][-1])
    
for r in result:
    print("Problem" , str(idx)+":" ,r)
    idx +=1