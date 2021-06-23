import sys
input = sys.stdin.readline

N ,M = map(int, input().split())

array = []

for i in range(N):
    temp_list = list(map(int, input().split()))
    array.append(min(temp_list))


print(max(array))