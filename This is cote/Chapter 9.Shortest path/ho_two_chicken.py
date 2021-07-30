import sys
from itertools import combinations
input =sys.stdin.readline

INF= 1e9

n,m = map(int, input().split())


distance= [[INF] *(n+1) for _ in range(n+1)]
building = [i for i in range(1,n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            distance[i][j]=0

for i in range(m):
    city_one , city_two = map(int,input().split())

    distance[city_one][city_two] = 2
    distance[city_two][city_one] = 2

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            distance[i][j] = min(distance[i][j], (distance[i][k] + distance[k][j]))

building_combination = list(combinations(building , 2))

result =[]
for i in range(len(building_combination)):
    cost  = 0
    
    candi_one , candi_two = building_combination[i][0],  building_combination[i][1]
    
    for j in range(1,n+1):
        cost += min(distance[j][candi_one] , distance[j][candi_two])

    result.append([cost,candi_one,candi_two])


result = sorted(result, key = lambda x :(x[0] , x[1] , x[2]))

print(result[0][1],result[0][2],result[0][0])