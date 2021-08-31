from collections import deque
def BFS(computers, computer_num, visited ,n):
    visited[computer_num] = True
    queue = deque()
    queue.append(computer_num)
    
    while len(queue) != 0:
        now = queue.popleft()
        visited[now] = True
        for i in range(n):
            if i == computer_num:
                continue
            
            if computers[now][i] == 1:
                if visited[i] == False:
                    queue.append(i)
    

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for computer_num in range(n):
        if visited[computer_num] == False:
            BFS(computers, computer_num, visited , n)
            answer += 1
    
    return answer

    





n = 3 
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n,computers))