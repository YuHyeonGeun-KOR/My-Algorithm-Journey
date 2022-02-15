def solution(n, lost, reserve):
    answer = n - len(lost)

    lost = list(map(int, lost))
    reserve = list(map(int, reserve))
    
    lost.sort()
    reserve.sort()
    for n in lost[:]:
        if n in reserve:
            reserve.remove(n)
            lost.remove(n)
            answer +=1
            
    for n in lost:
        if n-1 in reserve:
            reserve.remove(n-1)
            answer +=1
            continue
            
        if n+1 in reserve:
            reserve.remove(n+1)
            answer +=1
            continue
    
    return answer