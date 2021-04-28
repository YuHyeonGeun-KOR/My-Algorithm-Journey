import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
dx = [1,0,1]
dy = [0,1,1]                     

for i in range(t):
    n , m = map(int, input().split())
    posi = list(map(int, input().split()))
    Gold_Mountain = []
    
    for i in range(n):
        Gold_Mountain.append(posi[m*i:m*i+m])
    visited = [[0] * m for _ in range(n)]
    visited[i][0] = Gold_Mountain[i][0]
    for i in range(n):
        visited[i][0] = Gold_Mountain[i][0]    
    for i in range(1,m):
        for j in range(n):
            if j == 0 :
                visited[j][i] = Gold_Mountain[j][i] + max(visited[j][i-1] ,visited[j+1][i-1])
                
            elif j == n-1 :
                visited[j][i] = Gold_Mountain[j][i] + max(visited[j][i-1] ,visited[j-1][i-1])
                
            else:
                visited[j][i] = Gold_Mountain[j][i] + max(visited[j][i-1] ,visited[j-1][i-1],visited[j+1][i-1])    
               
    print(max(max(visited)))               