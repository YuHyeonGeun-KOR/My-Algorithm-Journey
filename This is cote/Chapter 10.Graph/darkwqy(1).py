def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_find(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else :
        parent[a] = b

n,m = map(int,input().split())
parent = [0] * (n+1)

edges = []
min_cost = 0

for i in range(1,n+1):
    parent[i] =i

for i in range(m):
    start,end,cost = map(int,input().split())
    edges.append((cost,start,end))

edges.sort()

cost_total = 0
for i in edges:
    cost , start, end = i
    cost_total+= cost
    if find_parent(parent,start) != find_parent(parent,end):
        union_find(parent,start,end)
        min_cost+=cost

print(cost_total -min_cost )
