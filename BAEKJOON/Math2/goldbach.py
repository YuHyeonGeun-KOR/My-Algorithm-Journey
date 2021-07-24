import sys
input = sys.stdin.readline

n= int(input())


m = int(10001**0.5)
prime = [True] * 10001
for i in range(2,m+1):
    if prime[i] == True:
        for j in range(i+i ,10001, i):
            prime[j] = False
prime[1] = False

for i in range(n):
    gold_num = int(input())
    for j in range(gold_num//2 , 1 , -1):
        if prime[j]  and prime[gold_num-j] :
            print(j,gold_num-j)
            break