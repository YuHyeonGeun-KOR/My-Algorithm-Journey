import sys
input = sys.stdin.readline

N ,M = map(int, input().split())
ball = list(map(int, input().split()))
ball_count = [0]* (M+1)


for i in ball:
    ball_count[i] += 1

result = 0
for i in range(1,M):
    for j in range(i+1,M+1):
        result += ball_count[i] * ball_count[j]
print(result)

from collections import deque
food_times = []
d = deque( food_times.sort())