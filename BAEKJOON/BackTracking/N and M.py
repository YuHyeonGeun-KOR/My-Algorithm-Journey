N, M = map(int, input().split()) 
visited = [0 for _ in range(N+1)] 
arr = [] 
def dfs(cnt): 
    if cnt == M: 
        print(arr) 
        return 
    for i in range(1,N+1): 
        if visited[i] == 0: 
            visited[i] = 1 
            arr.append(i) 
            
            dfs(cnt+1) 
            
            visited[i] = 0 
            arr.pop() 
            print(visited,cnt)
dfs(0)

