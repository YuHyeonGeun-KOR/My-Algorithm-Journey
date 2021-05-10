import sys


input = sys.stdin.readline
n = int(input())
m = int(input())

INF = 1e9
distance = [[INF] * (n+1) for _  in range(n+1)]

disco = [[] for _ in range(n+1)]

for i in range(m):
    start , end , cost = map(int, input().split())
    if distance[start][end] > cost:
        distance[start][end] =cost

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            distance[i][j] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            distance[i][j] = min (distance[i][j], distance[i][k] + distance[k][j])

for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        if distance[i][j] == INF:
            print(0,end =" ")
        else:
            print(distance[i][j],end =" ")
    print("")

