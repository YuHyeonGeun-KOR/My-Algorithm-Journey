n = int(input())

d = [0]*101

Food = list(map(int,input().split()))


d[0] = Food[0]
d[1] = max(Food[0],Food[1])

for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+Food[i])

print(d[n-1])

