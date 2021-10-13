import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

tree = {}
for i in range(n):
    root , left , right = input().rstrip().split()
    tree[root] = [[], []]
    tree[left] = [[], []]
    tree[right] = [[], []]
    if left != '.':
        tree[root][0].append(left)
    

    if right != '.':
        tree[root][1].append(right)

queue = deque(["A"])
result_pre= ""
result_mid = ""
result_nex = ""

while queue:
    root = queue.popleft()
    result_pre += root 

    if tree[root][0] != []:
        queue.appendleft(tree[root][0][0])

    if tree[root][1] != []:
        queue.append(tree[root][1][0])

queue = deque(["A"])
add_string = ''
while queue:
    root = queue.popleft()
    add_string += root 
    if tree[root][0] != []:
        queue.appendleft(tree[root][0][0]) 
    else:
        result_mid += add_string[::-1]
        add_string = ""

    if tree[root][1] != []:
        queue.append(tree[root][1][0])

  
queue = deque(["A"])
add_string = ''
while queue:
    root = queue.popleft()
    if tree[root][0] != [] and  tree[root][1] != []:
        queue.appendleft(tree[root][0][0]) 
        queue.append(tree[root][1][0])

    else:
        result_nex += root

if tree['A'][1] != [] and tree['A'][1][0]  not in result_nex:
    result_nex+=tree['A'][1][0]

if 'A' not in result_nex :
    result_nex += 'A'
print(result_pre)
print(result_mid)
print(result_nex)