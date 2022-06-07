import heapq
def solution(begin, target, words):
    answer = 0
    queue = []
    visited = [0] * len(words)
    
    heapq.heappush(queue , [0,begin])
    while queue:
        count , now = heapq.heappop(queue)
        if now == target :
            answer = count 
            break
        for i in range(len(words)):
            if visited[i] ==0:
                checksum = 0 
                for j in range(len(words[i])):
                    print()
                    if now[j] != words[i][j]:
                        checksum += 1
                if checksum == 1:
                    visited[i] = 1
                    heapq.heappush(queue ,[count +1 , words[i]])
    return answer

print(solution("hit" , "cog" , ["hot", "dot", "dog", "lot", "log", "cog"]))