def solution(citations):
    answer = 0
    result = []
    citations.sort()
    if max(citations) == 0:
        return 0
    for i in range(citations[-1]):
        h = 0
        for j in citations:
            if i <= j :
                h += 1
                if h == i:
                    result.append(h)
    
    result.sort()
    answer = result[-1]
    return answer