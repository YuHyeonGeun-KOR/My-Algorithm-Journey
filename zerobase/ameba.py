import heapq

def solution(delay, N):
    answer = 1
    queue = []
    heapq.heappush(queue, [0 , 0,True])
   
    while queue:
        now = heapq.heappop(queue)  
        if now[0] == N :
                continue  
        if now[2]:
            heapq.heappush(queue , [now[0] + 1, 0 ,True])
            heapq.heappush(queue , [now[0] + 1, 0 ,False])
            answer += 2
        else:
            
            if now[1] < delay:
                heapq.heappush(queue, [now[0]+1 , now[1] + 1 , False])
            elif now[1] == delay: 
                heapq.heappush(queue , [now[0] + 1 , 0 , True])
                heapq.heappush(queue , [now[0] + 1 , 0 , False])
                answer +=2
                     
    return answer



print(solution(1,2))