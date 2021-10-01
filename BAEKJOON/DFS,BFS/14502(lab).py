import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque
import copy

n,m = map(int, input().split())

lab = []
index = []
virus = []
safe_zone = []
index_num = 0

for i in range(n):
    lab.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        index.append((i,j))
        if lab[i][j] == 2:
            virus.append((i,j))

wall = list(combinations(index,3))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(wall_index):
    queue = deque()
    for i in virus:
        queue.append((i[0],i[1]))
    
    lab_copy = copy.deepcopy(lab)
    if lab_copy[wall_index[0][0]][wall_index[0][1]] ==0 and lab_copy[wall_index[1][0]][wall_index[1][1]] == 0 and lab_copy[wall_index[2][0]][wall_index[2][1]]==0:
        lab_copy[wall_index[0][0]][wall_index[0][1]] = 1
        lab_copy[wall_index[1][0]][wall_index[1][1]] = 1
        lab_copy[wall_index[2][0]][wall_index[2][1]] = 1
    else:
         return
    safe_num = 0

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0 <= ny < m and lab_copy[nx][ny] == 0:
                lab_copy[nx][ny] = 2
                queue.append((nx,ny))
        
    for i in range(n):
        for j in range(m):
            if lab_copy[i][j] == 0:
                safe_num+=1
    safe_zone.append(safe_num)
    
    return
for i in wall:
    bfs(i)

print(max(safe_zone))