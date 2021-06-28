import sys 
input = sys.stdin.readline
from collections import deque

n_queue = deque(input().rstrip())

result = 0

while(n_queue):
    next_num = n_queue.popleft()
    if result == 0 :
        result += int(next_num)
    else:
        if next_num != 0 :
            result *= int(next_num)

print(result)