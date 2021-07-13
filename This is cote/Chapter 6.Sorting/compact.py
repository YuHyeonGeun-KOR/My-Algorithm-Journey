import sys
input = sys.stdin.readline


n= int(input())
array = list(map(int, input().split()))
set_array = set(array)
sorted_array = sorted(set_array)
new_array = {}
for i in range(len(sorted_array)):
    new_array[sorted_array[i]] = i


for i in array:
    print(new_array[i] ,end= " ")