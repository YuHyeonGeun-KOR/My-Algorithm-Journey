from collections import deque

def solution(dartResult):
    answer = 0
    dartResult=list(dartResult)
    result = []
    temp = ""
    for dart in dartResult:
        x = dart
        if x != "S" and x != "D" and x != "T" and  x != "*" and x != "#":
            temp += x
            continue
            
        
        if x == "S":
            result.append(str(int(temp)))
            temp = ""
        elif x == "D":
            result.append(str(int(temp)**2))
            temp = ""
        elif x == "T":
            result.append(str(int(temp)**3))
            temp = ""
        elif x == "*":
            if len(result) == 1:
                result[0] += "*2"
            else:
                result[-1] += "*2"
                result[-2] += "*2"
            temp = ""    
        elif x == "#":
            result[-1] += "*(-1)"
            temp = ""
        
    for re in result:
        answer += eval(re)
    return answer