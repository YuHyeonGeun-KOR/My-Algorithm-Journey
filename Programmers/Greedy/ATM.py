n = int(input())

time = list(map(int,input().split()))
time = sorted(time)
start = 0
end = 0
result = 0
for i in range(n):
     result += sum(time[start:end+1])
     end +=1
print(result)