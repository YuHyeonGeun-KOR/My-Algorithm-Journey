import sys
from collections import deque
input = sys.stdin.readline

n= int(input())

board = []

queue = deque([[0,0]])

result = 0
visited = [[0] * n for _ in range(n)]

for i in range(n):
    board.append(list(map(int, input().split())))

  
for i in range(n):
    for j in range(n):
        if board[i][j] != 0 : 
            jump = board[i][j]
            if 0 <= i+jump < n :
                visited[i+jump][j] = visited[i][j] +1
            if 0 <= j + jump < n:
                visited[i][j+jump] = visited[i][j] +1
                
print(visited)
     

