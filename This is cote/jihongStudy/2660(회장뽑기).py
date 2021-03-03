from collections import deque
n = int(input())
candidate = [[] * (n+1) for i in range(n+1)] 
candidate_score = [0] * (n+1) 

result = 0

while(True):
    left,right = map(int,input().split())
    if left == -1 and right == -1:
        break
    else:
        candidate[left].append(right)
        candidate[right].append(left)

def dfs(x,result):
    if visited[x] ==0:
        visited[x] = result
        result += 1 

        for i in range (len(candidate[x])):
            dfs(candidate[x][i],result)
    else :
        return max(visited)



print(candidate)
for i in range(1,n+1):
    visited = [0]*(n+1)
    candidate_score[i] =  dfs(i,result)
    print(candidate_score[i])

print(candidate_score)







        
