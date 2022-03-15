from collections import deque
def solution(s):
    answer = -1
    
    origin = deque(s)
    q1 = deque()
    while origin:
        checker = origin.popleft()
        
        if not q1:
            q1.append(checker)
        else:
            if q1[-1] == checker:
                q1.pop()
            else:
                q1.append(checker)
    if q1 :
        answer = 0
    else:
        answer = 1         
    return answer