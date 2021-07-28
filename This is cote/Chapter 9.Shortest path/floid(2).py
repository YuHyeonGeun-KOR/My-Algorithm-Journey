import sys
input = sys.stdin.readline

n = int(input())

m = int(input())
INF = 1e9
cost_array = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j :
            cost_array[i][j] = 0

for i in range(m):

    start,end,cost = map(int, input().split())
    if  cost_array[start][end] > cost:
        cost_array[start][end] = cost

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            cost_array[i][j] = min (cost_array[i][j], cost_array[i][k] + cost_array[k][j])

for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        if cost_array[i][j] == INF:
            print(0,end =" ")
        else:
            print(cost_array[i][j],end =" ")
    print("")
