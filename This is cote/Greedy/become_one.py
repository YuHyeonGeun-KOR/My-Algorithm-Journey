N,K = map(int,input().split())
count = 0

while(1) :
    # N is divided by K and N is not 1 -> N / K 
    if N % K == 0 and N != 1:
        N = N // K
        count += 1
     # N is not divided by K and N is not 1 -> N - 1 
    elif N % K != 0 and N != 1 :
        N = N - 1
        count += 1
     # N is 1 -> break    
    elif N == 1 :
        break

print(count)