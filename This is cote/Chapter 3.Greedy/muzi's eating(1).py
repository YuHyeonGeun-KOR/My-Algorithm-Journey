def solution(food_times, k):
    count = 0

    def counter_set(count):
        if len(food_times)-1 < count:
            return 0
        else:
            return count
    
    def food_eat(count):
        if sum(food_times) == 0:
                return -1
        else :
            while(True):
                count = counter_set(count+1)
                if food_times[count] != 0:
                    return count 
                
    
    
    for i in range(k):
        if food_times[count] != 0 :
            food_times[count] -= 1
            
        else:
            count = food_eat(count)
            if count == -1:
                return(-1)
            else:
                food_times[count] -=1
        count = counter_set(count+1)

    count = food_eat(count)
    answer = count+1
    return answer



food_times = [4,2,4]
k = 8
print(solution(food_times,k))
