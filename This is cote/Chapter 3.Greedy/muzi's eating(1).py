from collections import deque
def solution(food_times, k):
    count = 0
    result = 0
    food_queue = deque()
    for i in range(len(food_times)):
        food_queue.append([i+1,food_times[i]])
    
    
    for i in range(k):
        if len(food_queue) == 0:
            result = -1 
            return result    
        index , food_num = food_queue.popleft()
        food_num -= 1

        if food_num != 0 :
            food_queue.append([index,food_num])                                                       
        else:
            continue
    index , food_num = food_queue.popleft()
    return index



food_times = [3,1,2]
k = 5
if solution(food_times,k) == -1:
    print(-1)
else:
    print(solution(food_times,k))


