def solution(gems):
    answer = []
    gem_count = set(gems)
    length_checker =0
    buy = dict()
    start = 0
    end = 0
    direc = "right"
    
    while end < len(gems) or not direc == "right" :
        if direc == "right":
            if gems[end] not in buy :
                buy[gems[end]] = 1
                length_checker += 1
            else :
                buy[gems[end]] += 1
            end += 1

        else :
            buy[gems[start]] -= 1
            if buy[gems[start]] == 0 :
                buy.pop(gems[start])
                length_checker -= 1
            start += 1

        if length_checker == len(gem_count) :
            direc = "left"
            answer.append([start+1,end])
        else :  
            direc = "right"
    answer = sorted(answer, key= lambda x: ((x[1]-x[0]), x[0]) )
    return answer [0]

        
gems =	 ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))