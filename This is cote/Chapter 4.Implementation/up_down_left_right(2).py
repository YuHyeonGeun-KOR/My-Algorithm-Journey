import sys 
from collections import deque
input  = sys.stdin.readline

N = int(input())

man = [1,1]
queue = deque(input().rstrip().split())

print(queue)
while(queue):
    direction = queue.popleft()
    if direction == 'U' and man[0] != 1:
        man[0] -= 1 
    elif direction == 'D' and man[0] != N:
        man[0] += 1 
    elif direction == 'L' and man[1] != 1:
        man[1] -= 1 
    elif direction =='R' and man[1] != N:    
        man[1] += 1


print(man[0], man[1])