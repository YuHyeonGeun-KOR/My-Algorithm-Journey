import sys
input = sys.stdin.readline

t ,w = map(int, input().split())

jado = []
for i in range(t):
    jado.append(int(input()))

dp = [[0] * (len(jado) + 1 ) for _ in range(w+1)]

for i in range(1, len(jado)+1):
    if jado[i-1] == 1:
        dp[0][i] = dp[0][i-1] + 1
    else:
        dp[0][i] = dp[0][i-1]



for i in range(1,w+1):
    for j in range(1, t +1 ):
        if jado[j-1] == 1 and i % 2 == 0:
            dp[i][j] = max(dp[i][j-1] , dp[i-1][j] ) + 1 
        elif jado[j-1] == 2 and i % 2 == 1:
            dp[i][j] = max(dp[i][j-1] , dp[i-1][j]) + 1
        else:
            dp[i][j]  = max(dp[i][j-1] , dp[i-1][j])

print(dp[-1][-1])