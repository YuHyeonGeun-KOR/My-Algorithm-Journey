N,M = map(int, input().split())

d = [10001] * (M+1)
d[0] = 0
coin =[]

for i in range(N):
    coin.append(int(input()))

for i in range(N):
    for j in range(coin[i],M+1):
        if d[j - coin[i]] != 10001 :
            d[j] = min(d[j] , d[j-coin[i]]+1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])