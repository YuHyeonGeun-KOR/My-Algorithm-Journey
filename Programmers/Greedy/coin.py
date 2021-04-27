n,k = map(int,input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

coin.reverse()

count = 0
for i in coin:
    if k//i >= 1:
        count += k//i
        k = k % i 
print(count)