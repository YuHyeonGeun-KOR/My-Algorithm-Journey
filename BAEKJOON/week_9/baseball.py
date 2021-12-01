import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline

n= int(input())

visited = set()
result = 0
def cal_score(order , member):
    score = 0 
    global result
    hit_num = 0
    for i in range(n):
        out_count = 3
        base = 0
        lineup = order[:3] + (1,) + order[3:]
        line_idx = 0 
        while out_count > 0:
            if member[i][lineup[line_idx]] != 0:
                base = (base << member[i][lineup[line_idx]] ) | (1 << member[i][lineup[line_idx]]  - 1)
                score += (base >> 3 & 1) + (base >> 4 & 1) + (base >> 5 & 1) + (base >> 6 & 1)
                base &= 7
            else:
                out_count -= 1
        
            line_idx = (line_idx + 1) % 9 
          
    result = max(result , score)

member = [{} for _ in range(n)]
inning = 0
for i in range(n):
    score = deque(map(int, input().split()))
    idx = 1
    for s in score:
        member[inning][idx] = s
        idx +=1
    inning +=1
    

m_order = [1,2,3,4,5,6,7,8,9]
m_order_per = list(permutations(m_order , len(m_order)))

for m_p in m_order_per:
    cal_score(m_p , member)
print(result)

    

