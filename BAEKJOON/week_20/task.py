import heapq
from collections import deque

 
def solution(jobs):
    answer = 0
    jobs= sorted(jobs , key = lambda x : (x[0],x[1]))
    jobs_queue = deque(jobs)
    
    job_count = len(jobs)
    time = 0
    start = jobs_queue.popleft()
    task_sum = start[1]
    time += start[0] + start[1]
    
    while jobs_queue:
        if jobs_queue[0][0] >= time:
            time = jobs_queue[0][0] + jobs_queue[0][1]
            task_sum += jobs_queue[0][1]
            jobs_queue.popleft()
        else:
            temp_queue = []
            while jobs_queue:
                if jobs_queue[0][0] <= time:
                    j = jobs_queue.popleft()
                    heapq.heappush(temp_queue, [j[1], j[0]])
                else:
                    break
            time += temp_queue[0][0]
            task_sum += time - temp_queue[0][1]
            heapq.heappop(temp_queue)
            while temp_queue:
                t = temp_queue.pop()
                jobs_queue.appendleft([t[1] , t[0]])
    answer = task_sum // job_count
    return answer


jobs =[[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
print(solution(jobs))