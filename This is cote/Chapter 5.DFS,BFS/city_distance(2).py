from collections import deque
import sys
input = sys.stdin.readline
n,m,k,start = map(int, input().split())

visited =[False]*(n+1)
Bridge = [[] * (n+1) for i in range(n+1)] 
distance = [0]*(n+1)

for i in range(m):
    left,right = map(int, input().split())
    Bridge[left].append(right)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    distance_cnt = 0
    while queue:
        x = queue.popleft()
        distance_cnt += 1
        for i in Bridge[x]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[x]+1
    
bfs(start)

if k not in distance:
    print(-1)
else:    
    for i in range(len(distance)):
        if distance[i] == k:
            print(i)
