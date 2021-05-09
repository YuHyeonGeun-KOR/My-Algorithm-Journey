def solution(s):
    answer = 0
    result = ''
    number = {'zero' : 0 , 'one': 1 ,'two': 2, 'three': 3 ,'four': 4 ,'five': 5,'six': 6 ,'seven': 7 ,'eight': 8 ,'nine': 9  }
    alpha = ''
    for i in s:
        if i.isdigit(): 
            result += str(i)
        else:
            alpha += i
            if alpha in number:
                result += str(number[alpha])
                alpha = ''
    
    answer = result
    return int(answer)

s = 'one4seveneight'

print(solution(s))