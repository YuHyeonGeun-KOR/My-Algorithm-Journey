import sys

input = sys.stdin.readline


prime_array = [True] * 300001
m = int(300001**0.5)
for i in range(2,m+1):
    if prime_array[i] == True:
        for j in range(i+i, 300001,i):
            prime_array[j] = False
prime_array[1] = False

    

answer = []

while True:
    n= int(input())
    
    count = 0 
    if n == 0:
        break
    else:
        for i in range(n+1,2*n+1):
            if prime_array[i] == True:
                count += 1

        answer.append(count)



for i in (answer):
    print(i)