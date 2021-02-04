def solution(v):
    answer = []
    x_a = []
    y_a = []
    for i in v:
        if i[0] not in x_a:
            x_a.append(i[0])
        else :
            x_a.remove(i[0])
        
        if i[1] not in y_a:
            y_a.append(i[1])
        else :
            y_a.remove(i[1])
    anwser = x_a + y_a 
    return answer

