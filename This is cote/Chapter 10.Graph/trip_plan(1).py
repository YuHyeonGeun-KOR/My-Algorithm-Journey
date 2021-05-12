import sys
input = sys.stdin.readline
n,m = map(int,input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a

parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] =i

node_list = []

for i in range(n):
    node_list.append(list(map(int,input().split())))

for i in range(n):
    for j in range(i,n):
        if node_list[i][j] == 1 :
            union_parent(parent,i+1,j+1)
input = list(map(int,input().split()))

answer = "YES"
for i in range(m-1):
    if find_parent(parent,input[i]) != find_parent(parent,input[i]):
        answer = "NO"
        break
print(answer)

