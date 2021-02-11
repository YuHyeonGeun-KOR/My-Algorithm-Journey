def solution(participant, completion):
    answer = ''
    count = {}
    
    for i in participant:
        try: count[i] += 1
        except: count[i] = 1
    
    for i in completion:
        count[i] -= 1  
    
    for part, compl in count.items():
        if compl != 0:
            answer = part
    
    return answer