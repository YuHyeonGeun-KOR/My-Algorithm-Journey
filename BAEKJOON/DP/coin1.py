import sys
from collections import deque
sys.setrecursionlimit(15000)
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0] * (k+1) 
dp[0] = 1 
coin = []
for i in range(n):
    coin.append(int(input()))

for c in  coin:
    for i in range(c , k+1):
        dp[i] = dp[i] + dp[i-c]

print(dp[k])    
    
