import sys 
input = sys.stdin.readline
INF = float('inf') 

n,m = map(int,input().split())
A = [0]*n
for i in range(n):
    A[i] = int(input())

A.sort()
start = 0
end = 1

result = INF
while start < n and end < n:
        if A[end]-A[start]<m:
            end+=1
        elif A[end]-A[start] == m:
            result = m
            break
        else:
            if (A[end]-A[start]) < result:
                result = (A[end]-A[start])
            start+=1
    
print(result)

                    
