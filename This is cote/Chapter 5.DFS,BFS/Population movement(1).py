from collections import deque
N,L,R = map(int,input().split())

nation = []
visited_checker = [[0]*N for _ in range(N)]
result = 0 

dx = [0,-1,0,1]
dy = [1,0,-1,0]
for i in range(N):
    nation.append(list(map(int,input().split())))


def bfs(x,y,visited):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()

        for i in range (4):
            xx = x + dx[i]
            yy = y + dy[i]

            if xx <= -1 or xx >= N or yy <= -1 or yy >= N or visited[xx][yy] == 1:
                continue 
            elif L <= abs(nation[x][y] - nation[xx][yy]) <= R and visited[xx][yy] == 0:
                visited[x][y] = 1
                visited[xx][yy] = 1
                queue.append((xx,yy))
    
    return visited


def movement(visited):
    sum = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                sum += nation[i][j]
                cnt +=1
    r = sum//cnt
    print(sum,cnt,r)
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                nation[i][j] = r
    return
    


for i in range(2000):
    visited = [[0]*N for _ in range(N)]
    for j in range(N):
        for k in range(N):        
            checker = bfs(j,k,visited)
    if visited_checker != checker :
        print(checker)
        movement(visited)
        print(nation)
        result += 1
    else: 
        break                


print(result)   
