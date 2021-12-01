import sys
import heapq
input = sys.stdin.readline

n,k = map(int, input().split())

time = 0 
queue = []
heapq.heappush(queue , [0,n])
visited = set()
while queue:
    t , x = heapq.heappop(queue)
    
    if x == k:
        print(t)
        break
    if x*2 <= 100000 and x*2 not in visited:
    
        visited.add(2*x)
        heapq.heappush(queue, [t, x*2])
    if x+1 not in visited and n+1 <= 100000:
        visited.add(x+1)
        heapq.heappush(queue, [t+1 , x+1])
    if x-1 not in visited and x-1 >=0:
        visited.add(x-1)
        heapq.heappush(queue, [t+1 , x-1])


