import sys

input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))


temp_max = -1111
for i in range(1,n):
    num_list[i] = max(num_list[i] , num_list[i] + num_list[i-1])
   
        
print(max(num_list))