import sys 
import copy
input = sys.stdin.readline

sys.setrecursionlimit(100000)


N = int(input())

area = []
max_num = 0

for i in range(N):
    area.append(list(map(int, input().split())))
    for j in range(N):
        if area[i][j] > max_num:
            max_num = area[i][j]
def dfs (x,y,h,area_copy):
    if x <= -1 or x >= N or y <=-1 or y >= N:
        return False
    
    if area_copy[x][y] > h: 
        area_copy[x][y] = 0
        dfs(x+1,y,h,area_copy)
        dfs(x-1,y,h,area_copy)
        dfs(x,y+1,h,area_copy)
        dfs(x,y-1,h,area_copy)
        return True
        
    return False


for i in range(max_num):
    
    area_copy = copy.deepcopy(area)
    count = 0 
    result = 0
    for j in range(N):
        for k in range(N):
            if dfs(j,k,i,area_copy) == True:
                count +=1

    result = max(result, count)

print(result)