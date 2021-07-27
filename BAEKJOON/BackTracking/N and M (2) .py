import sys 
inpur = sys.stdin.readline

n,m = map(int, input().split())

arr = []
start_idx =1
visited = [0] * (n+1)
def dfs (start_idx):
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(start_idx, n+1):
        
        if visited[i] == 0:
            arr.append(i)
            visited[i] = 1

            dfs(i+1)
            arr.pop()
            visited[i] = 0
            
            


dfs(start_idx)
