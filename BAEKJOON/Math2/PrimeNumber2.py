import sys
input = sys.stdin.readline

prime = [True] * 10001


m = int(10001 ** 0.5)

for i in range(2,m+1):
    if prime[i] == True:
        for j in range(i+i, 10001 , i):
            prime[j] = False;
prime[1] = False
N = int(input())
M = int(input())

result = []


for i in range(N,M+1):
    if prime[i] == True:
        result.append(i)

if len(result) == 0 :
    print(-1)
else:
    print(sum(result))
    print(result[0])