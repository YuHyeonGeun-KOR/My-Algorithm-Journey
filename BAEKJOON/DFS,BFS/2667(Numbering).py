n = int(input())

MapPaper = [list(map(int, input())) for _ in range(n) ] 

result = 0
Complex = 0

housecheck = [0]
house = []


def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False  
    if MapPaper[x][y] == 1:
        MapPaper[x][y] = 0        
        housecheck[0] += 1
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x+1,y)
        return True
    else :
        return False
    
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            Complex += 1   
            house.append(housecheck[0])
            housecheck[0] = 0
house.sort()
print(Complex)
for i in house:
    print(i)