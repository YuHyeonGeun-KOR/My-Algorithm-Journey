import sys 
import copy
sys.setrecursionlimit(100000)
input = sys.stdin.readline

array_color = []
array_color_second = []
n = int(input())

for i in range(n):
    array_color.append(list(input().rstrip()))

array_color_second = copy.deepcopy(array_color)


def dfs_R(x,y,array):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if array[x][y] == "R":
        array[x][y] = 1        
        dfs_R(x,y-1,array)
        dfs_R(x,y+1,array)
        dfs_R(x-1,y,array)
        dfs_R(x+1,y,array)
        return True
    else :
        return False    

def dfs_G(x,y,array):
    
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if array[x][y] == "G":
        array[x][y] = 1        
        dfs_G(x,y-1,array)
        dfs_G(x,y+1,array)
        dfs_G(x-1,y,array)
        dfs_G(x+1,y,array)
        return True
    else :
        return False    

def dfs_B(x,y,array):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if array[x][y] == "B":
        array[x][y] = 1        
        dfs_B(x,y-1,array)
        dfs_B(x,y+1,array)
        dfs_B(x-1,y,array)
        dfs_B(x+1,y,array)
        return True
    else :
        return False    



result_R = 0
result_G = 0
result_B = 0
result_R_G = 0


for i in range(n):
    for j in range(n):
        if dfs_R(i,j,array_color) == True:
            result_R += 1


for i in range(n):
    for j in range(n):
        if dfs_G(i,j,array_color) == True:
            result_G += 1
            
for i in range(n):
    for j in range(n):
        if dfs_B(i,j,array_color) == True:
            result_B += 1

for i in range(n):
    for j in range(n):
        if array_color_second[i][j] == "R":
            array_color_second[i][j] = "G"



for i in range(n):
    for j in range(n):
        if dfs_G(i,j,array_color_second) == True:
            result_R_G += 1


print(result_B+result_G+result_R , result_B+result_R_G)