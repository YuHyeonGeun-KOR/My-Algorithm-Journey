import sys

num =int(sys.stdin.readline())

arr = [] 

for i in range(num):
    arr.append(int(sys.stdin.readline()))

arr.sort()


for j in range(len(arr)):
    print(arr[j])