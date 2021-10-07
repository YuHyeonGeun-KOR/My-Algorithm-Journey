import sys
from collections import deque
from typing import ChainMap
input = sys.stdin.readline

t = int(input())

def bfs(a,b):
    test_queue =deque()
    test_queue.append([a, ""])
    target = b
    visited = [0] * 10000
    visited[a] = 1
    while test_queue:
        checker ,used_cmd = test_queue.popleft()
        

        if checker == target :
            return used_cmd

      
        if checker * 2 > 9999 and visited[checker*2 % 10000] == 0:
            visited[checker*2 % 10000] = 1
            test_queue.append([checker*2 % 10000 , used_cmd + "D"])
        
        if checker * 2 <= 9999 and visited[checker * 2] == 0:
            visited[checker*2] =1
            test_queue.append([checker*2 , used_cmd + "D"])
        
        if checker -1 <0  and visited[9999] == 0:
            visited[9999] = 1
            test_queue.append([9999, used_cmd + "S"])
        
        if checker -1 >= 0 and visited[checker - 1 ] == 0:
            visited[checker-1] = 1
            test_queue.append([checker-1 ,  used_cmd + "S"])

        
        if checker < 10:
            string_checker = "000" + str(checker)
        elif checker < 100:
            string_checker = "00"+ str(checker)
        elif checker <1000:
            string_checker = "0" +str(checker)
        else:
            string_checker = str(checker)
        L_string_checker = string_checker[1] + string_checker[2] + string_checker[3] + string_checker[0]
        R_string_checker = string_checker[3] + string_checker[0] + string_checker[1] + string_checker[2]
        
        if visited[int(L_string_checker)] == 0:
            visited[int(L_string_checker)] = 1
            test_queue.append([int(L_string_checker) , used_cmd + "L"])
        if visited[int(R_string_checker)] == 0:
            visited[int(R_string_checker)] = 1
            test_queue.append([int(R_string_checker) , used_cmd + "R"])


        
result = []
for i in range(t):
    a , b = map(int, input().split())
    print(bfs(a,b))

