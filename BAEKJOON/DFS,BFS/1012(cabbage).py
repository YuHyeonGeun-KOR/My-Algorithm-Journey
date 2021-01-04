import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

n = int(input())



bugs = [0]*n

def dfs (x_n,y_n,x,y):
    if x_n < 0 or x_n >= x or y_n < 0 or y_n >= y :
        return False
    
    if field[y_n][x_n] == 1:
        field[y_n][x_n] = 0
        dfs(x_n-1,y_n,x,y)
        dfs(x_n,y_n-1,x,y)
        dfs(x_n+1,y_n,x,y)
        dfs(x_n,y_n+1,x,y)
        return True
    else:
        return False 

for i in range(n):
    x,y,k = map(int,input().split())

    field = [[0]*(x+3) for i in range(y+3)]
    bug = 0

    
    
    for _ in range(0,k):
        a,b = map(int, input().split())
        field[b][a] = 1

 

    for l in range(0,x):
        for m in range(0,y):
            if dfs(l,m,x,y) == True:
                bug += 1

    bugs[i] = bug

for i in range(0,n):
    print(bugs[i])




