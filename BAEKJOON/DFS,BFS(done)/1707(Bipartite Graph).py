from collections import deque
import sys 
input = sys.stdin.readline

n= int(input())

result = []

def bfs(start):
    bip[start] = 1
    queue = deque()
    queue.append(start)    

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if bip[i] == 0:
                bip[i] = -bip[a]
                queue.append(i)
            else:
                if bip[i] == bip[a]:
                    return False
    return True



for i in range(n):
    v,e = map(int,input().split())
    graph = [[] for i in range(v)]
    bip = [0] * (v)
    anwser = "YES"
    for i in range(e):
        a,b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    for i in range(v):
        if bip[i] == 0:
            if bfs(i) == False:
                anwser = "NO"
                break

        
    result.append(anwser)


for i in result:
    print(i)