import heapq
import sys

input = sys.stdin.readline
queue = []
queue_left = []
queue_right  = []

n = int(input())
result = []
for i in range(n):
    x = int(input())
    if len(queue_right) == len(queue_left):
        heapq.heappush(queue_right, -x)
    else:
        heapq.heappush(queue_left, x)

    if len(queue_right) >= 1 and len(queue_left) >= 1 and queue_right[0] * -1 > queue_left[0]:
        max_value = heapq.heappop(queue_right) * -1
        min_value = heapq.heappop(queue_left)
        
        heapq.heappush(queue_right, min_value * -1)
        heapq.heappush(queue_left, max_value)

    print(queue_right[0] * -1)

