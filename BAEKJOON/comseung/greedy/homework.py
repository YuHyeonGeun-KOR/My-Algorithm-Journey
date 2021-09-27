import sys
from collections import deque
input = sys.stdin.readline

n= int(input())

work_list = []

for i in range(n):
    work_list.append(list(map(int,input().split())))


work_list = sorted(work_list , key = lambda x : -x[1])

work_list = deque(work_list)
to_do_list = [0] * (1001)

while work_list:
    work = work_list.popleft()
    day, score = work[0] , work[1]
    while True:
        if to_do_list[day] == 0:
            to_do_list[day] = score
            break
        else:
            day -= 1
            if day == 0:
                break

print(sum(to_do_list))
