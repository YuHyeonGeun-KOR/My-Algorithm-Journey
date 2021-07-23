n= int(input())

result = []

prime = [True] * 10000001


m = int(10000001 ** 0.5)

for i in range(2,m+1):
    if prime[i] == True:
        for j in range(i+i, 10000001 , i):
            prime[j] = False;
prime[1] = False

prime_number = []

for i in range(2,10000001):
    if prime[i] == True:
        prime_number.append(i)
prime_idx = 0   

while prime_number[prime_idx] <= n:
   
    if n % prime_number[prime_idx] == 0:
        print(prime_number[prime_idx])
        n = n // prime_number[prime_idx]
    else:
        prime_idx += 1  