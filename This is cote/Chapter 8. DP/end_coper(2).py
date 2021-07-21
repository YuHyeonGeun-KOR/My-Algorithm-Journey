import sys

input = sys.stdin.readline

n = int(input())

timeList = []
for i in range(n):
    timeList.append(list(map(int, input().split())))

income = [0] *(n+5)
max_income = 0

for i in range (len(timeList)):
    
    if income[i] > income[i+1]:
        income[i+1] = income[i]
    income[i+timeList[i][0]] = max((income[i] + timeList[i][1]) , income[i+timeList[i][0]] ) 
    
print(max(income[:n+1]))