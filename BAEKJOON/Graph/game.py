import sys
input = sys.stdin.readline

n = int(input())

parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(x)
    return parent[x]

def union(parent , a , b):
    root_a = find_parent(a)
    root_b = find_parent(b)

    if root_a > root_b:
        parent[root_b] =  root_a
    else:
        parent[root_a] = root_b


graph = []
road_map = []
for i in range(n):
    input_list = list(map(int, input().split()))
    road_map.append(input_list)

    if i == 0 :
        graph.append([input_list[0] , 0 , 1 ])
    else:
        graph.append([input_list[0] , i, input_list[1]])
            

            
graph.sort()

for g in graph:
    cost, a , b = g
    if find_parent(a) != find_parent(b):
        union(parent , a ,b)
    
print(graph)
print(parent)
