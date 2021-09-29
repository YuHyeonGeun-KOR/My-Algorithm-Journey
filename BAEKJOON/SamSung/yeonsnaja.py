import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline

n = int(input())
operator = {0 : "+" , 1 : "-" , 2 : "//" , 3 : "*"}
operator_list = []

number_list = list(map(int, input().split()))
operator_num_list = list(map(int, input().split()))
idx = 0 

for i in operator_num_list:
    for j in range(i):
        operator_list.append(operator[idx])
    idx += 1

operator_lists  = list(permutations(operator_list ,  len(operator_list)))

result = []
for operator_list  in operator_lists:
    num_queue = deque(number_list)
    op_queue = deque(operator_list)
    total = num_queue.popleft()
    while op_queue:
        op = op_queue.popleft()
        if op == "+":
            total = total + num_queue.popleft()
        elif op == "-":
            total = total - num_queue.popleft()
        elif op == "//":
            total = int(abs(total) / num_queue.popleft())
        else :
            total = total * num_queue.popleft()
        
    result.append(total)
print(max(result))
print(min(result))
