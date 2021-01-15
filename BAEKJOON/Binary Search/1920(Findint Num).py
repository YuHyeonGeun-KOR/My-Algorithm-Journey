def solution(citations):
    answer = 0
    result = []
    citations.sort()
    print(critations)
    for i in range(citations[-1]):
        h = 0
        for j in citations:
            if i <= j :
                h += 1
                if h == i:
                    result.append(h)
    
    result.sort()
    print(result)
    answer = result[-1]
    return answer

critations = [4,1,2,7,8]

print(solution(critations))

