def solution(N, stages):
    answer = []
    count = [0] * (N+2)

    for i in stages:
        count[i] += 1
    
    ch = count[N+1]
    rate = []


    
    for i in range(N,0,-1):
        ch += count[i]
        if ch == 0:
            rate.append([i, 0])
        else:
            rate.append([i, count[i]/ch])

    result = sorted(rate,key = lambda x : (-x[1],x[0]))
    
    for i in result:
        answer.append(i[0])
    
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N,stages))