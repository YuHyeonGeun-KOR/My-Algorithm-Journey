import sys
input = sys.stdin.readline

n = int(input())

distance = [0] * (2*n + 1)

for i in range(n): 
    dis =  int(input())
    distance[i+1] = dis
    distance[i+n+1] = dis

for i in range(1, 2*n):
    distance[i] += distance[i-1]

result = 0 
for i in range(n+1):
    for j in range(i - n + 1, n):
        result = max( result , min(distance[j] - distance[i] , distance[i+n] - distance[j]))

print(result)