import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
result = []
for i in range(n):
    s = input().rstrip()
    left_index = 0
    right_index = len(s) - 1
    counter_1 = 0
    counter_2 = 0
    
    while(left_index < right_index):
        if s[left_index] != s[right_index]:
            break
        else:
            left_index += 1    
            right_index -= 1

    left_index_plus = left_index + 1  
    r1 = right_index
    right_index_plus = right_index - 1 
    l1 = left_index

    while(left_index_plus < r1):
        counter_1 = 1
        if s[left_index_plus] != s[r1]:
            counter_1 =2
            break
        else:
            left_index_plus += 1    
            r1 -= 1

    while(l1 < right_index_plus):
        counter_2 =1
        if s[l1] != s[right_index_plus]:
            counter_2 =2
            break
        else:
            l1 += 1    
            right_index_plus -= 1

            
    if counter_1 == 0 and counter_2 == 0 :
        result.append(0)
    elif counter_1 == 1 or counter_2 == 1:
        result.append(1)
    else:
        result.append(2)


for i in result:
    print(i)
