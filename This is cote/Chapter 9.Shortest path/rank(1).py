from collections import deque
n,m = map(int,input().split())
INF = 1e9
check = [[INF] * (n+1)  for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            check[i][j] = 0

for i in range(m):
    left,right  = map(int,input().split())
    check[right][left] = 1
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            check[i][j] = min(check[i][j], check[i][k]+ check[k][j])
count = 0 
for i in range(1,n+1):
    len_check = 0
    for j in range(1,n+1):
        if check[i][j] != INF or check[j][i] != INF:
            len_check +=1
    if len_check == n:
        count +=1
print(count)
    
 
