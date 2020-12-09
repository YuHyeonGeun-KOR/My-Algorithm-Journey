N,M = map(int,input().split())

graph = [[int(x) for x in input()] for _ in range(N)]

result = 0
print(graph)
def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False  
    if graph[x][y] == 0:
        graph[x][y] = 1        
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x+1,y)
        return True
    else :
        return False    

for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result += 1

print(result)