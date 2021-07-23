N , M = map(int, input().split())
result = []

prime = [True] * 10000001


m = int(10000001 ** 0.5)

for i in range(2,m+1):
    if prime[i] == True:
        for j in range(i+i, 10000001 , i):
            prime[j] = False;
prime[1] = False

for i in range(N,M+1):
    if prime[i] == True:
        print(i)