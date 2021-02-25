from itertools import combinations

n = int(input())

first_line = []
second_line = []
check = []
result = []
for i in range(n):
    first_line.append(i+1)
    second_line.append(int(input()))

for i in range(1,n+1):
    check = list(combinations(first_line,i))
    for j in 
print(first_line)
print(second_line)


