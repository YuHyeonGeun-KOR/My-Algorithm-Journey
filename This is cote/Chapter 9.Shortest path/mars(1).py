import sys
import heapq
from collections import deque
input = sys.stdin.readline
t = int(input())


INF = int(1e9)
dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = []    
for i in range(t):
    n= int(input())
    cost = [[INF]*n for _ in range(n)]

    board = []
    for col in range(n):
        board.append(list(map(int, input().split())))
    check_que = [(board[0][0] , 0,0)]
    cost[0][0] = board[0][0]

    while check_que:
        c,x,y = heapq.heappop(check_que)
        
        for j in range(4):
            xx = x+dx[j]
            yy = y+dy[j]
            if 0 <= xx < n and 0 <= yy < n :
                
                temp_cost = board[xx][yy] + c
                if xx == n-1 and yy == n-1:
                    cost[xx][yy] = temp_cost
                    check_que = ()
                elif cost[xx][yy] > temp_cost:
                    cost[xx][yy] = temp_cost
                    heapq.heappush(check_que,(temp_cost,xx,yy))
    print(cost)
    result.append(cost[-1][-1])

for i in range(t):
    print(result[i])
        
        
