N,K = map(int , input().split())

A= list(map(int , input().split()))
B= list(map(int , input().split()))

A.sort()
B.sort(reverse= True)

for i in range(K):
    if A[i] < B[i]:
        A[i],B[i] = B[i],A[i]
    else:
        break
    
result=0
for i in A:
    result += i

print(result)    
