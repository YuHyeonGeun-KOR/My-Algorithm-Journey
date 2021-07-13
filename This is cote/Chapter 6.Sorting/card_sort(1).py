import sys 
input = sys.stdin.readline

n = int(input())

num = []
for i in range(n):
    num.append(int(input()))

num.sort()

temp = []
temp_sum = num[0] + num[1]
temp.append(temp_sum)
for i in range(2,n):
    temp_sum += num[i]
    temp.append(temp_sum)
    print(temp_sum)
    print(temp)

print(sum(temp))
