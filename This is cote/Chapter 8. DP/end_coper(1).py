n = int(input())

work = {}
for i in range(n):
    work[i+1] = list(map(int,input().split())) 1: [3 , 10]

start_to_end_income = [0] * (10000)
time = 0
income =0
result = []
for i in range(1,n+1):
    time = work[i][0]
    income = work[i][1]
    if start_to_end_income[i] > start_to_end_income[i+1]:
        start_to_end_income[i+1] = start_to_end_income[i]

    if start_to_end_income[time + i] < start_to_end_income[i] + income:
         start_to_end_income[time + i] = start_to_end_income[i] + income
    


        
print(start_to_end_income[n+1])