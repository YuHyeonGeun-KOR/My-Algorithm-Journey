import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
candi = list(map(int,input().split()))

num = 0
candi.sort()
count = 0 
candi_queue = deque(candi)
while(candi_queue):
    leader = candi_queue.popleft()
    if candi_queue:
        if leader == 1:
            count +=1
        else:
            checker = 1
            for i in range(leader-1):
                member = candi_queue.popleft()
                if member == leader:
                    checker +=1
                else:
                    candi_queue.appendleft(member)

            if checker == leader:
                count +=1
print(count)    