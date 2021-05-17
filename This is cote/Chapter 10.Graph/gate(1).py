import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] =b


gate = int(input())
airplane = int(input())

parent = [0] * (gate+1)

for i in range(1,gate+1):
    parent[i] = i

c = 0 

for i in range(airplane):
    airplane_number = int(input())
    root_checker = find_parent(parent,airplane_number)
    if root_checker == 0 :
        break
    union_parent(parent,root_checker,root_checker-1)
    c +=1

print(c)