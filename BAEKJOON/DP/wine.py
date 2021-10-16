import sys
input = sys.stdin.readline

n = int(input())

wine = []
for i in range(n):
    wine.append(int(input()))

dp = []

dp.append(wine[0])
if n >1:
    dp.append(wine[0]+ wine[1])
if n >2:
    dp.append(max(wine[2] + wine[1] , wine[0] + wine[2] , dp[1]))
if n >3:
    for i in range(3, n):
        dp.append(max(dp[i-3] + wine[i-1] + wine[i] , dp[i-2] + wine[i] , dp[i-1]) )

print(dp[-1])





