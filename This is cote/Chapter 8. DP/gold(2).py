import sys
imput = sys.stdin.readline

T = int(input())

answer =[]
for _ in range(T):
    goldSum = 0
    inputArray = []
    goldArray = []
    n,m = map(int, input().split())
    
    inputArray = list(map(int, input().split()))

    for i in range(n):
        goldArray.append(inputArray[m*i:m*i+m])

    result = [[0] *(m) for _ in range(n)]     
    dx = [-1,0,1]
    
    for i in range(n):
        result[i][0] = goldArray[i][0]

        
    for j in range(1,m):
        for i in range(n):
            for idx in range(3):
                nx = i+dx[idx]
                
                if nx <= -1 or nx >= n:
                    continue

                result[i][j] = max(result[i][j] , (result[nx][j-1] + goldArray[i][j]))
                    
    max_gold = 0
    for i in range(n):
        max_gold = max(max_gold , result[i][-1])    

    answer.append(max_gold)

for i in answer:
    print(i)