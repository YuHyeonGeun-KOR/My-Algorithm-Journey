def solution(s):
    answer = len(s)
    
    for step in range(1,len(s)//2+1):
        result =""
        left = s[0:step]
        counter = 1
        
        for window in range(step,len(s),step):
            right = s[window:step+window]
            
            if left == right :
                counter += 1
            else:
                if counter >= 2:
                    result = result + str(counter) + left
                    
                else:
                    result = result + left
                
                
                left = right
                counter = 1         
            
        if counter >= 2:
            result += str(counter) + left
        else:
            result += left
        answer = min(answer, len(result))
    return answer


    
s = "aabbaccc"
print(solution(s))