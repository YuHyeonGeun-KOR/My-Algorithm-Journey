import sys
from collections import deque
import copy
input = sys.stdin.readline

n, k = map(int, input().split())

result  = {}

for i in range(k+2):
    result[i] = []
queue = deque()

result[0].append(str(n))

queue.append([0 , list(str(n))])
temp = ""

def list_to_str(list):
    s = ""
    for i in list:
        s += i
    return s

while queue:
    cnt , num_list = queue.popleft()
    
    if cnt == k :
        continue
    for i in range(len(num_list)-1):
        for j in range(i+1 , len(num_list)):
            num_list[i] , num_list[j] = num_list[j] ,  num_list[i]
            num_string = list_to_str(num_list)
            
            if num_string not in result[cnt+1] and num_list[0] != "0":
                result[cnt+1].append(num_string)
                queue.append([cnt+1, list(num_string)] )
            num_list[i] , num_list[j] = num_list[j] ,  num_list[i]
    

if len(result[k]) == 0:
    print(-1)
else:
    print(max(result[k]))

