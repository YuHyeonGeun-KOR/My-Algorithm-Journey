import sys
input = sys.stdin.readline


def b_search(array, target,start,end):
    while start <= end:
        mid = (start+end) //2
        if array[mid] > target :
            end = mid -1
        elif array[mid] < target:
            start = mid + 1
        else:
            return True

    return False

n = int(input())

array  = list(map(int, input().split()))
array = sorted(array)
m = int(input())

target_list = list(map(int, input().split()))

result = []

for i in range(m):
    result.append(b_search(array , target_list[i] , 0, n))

for i in result:
    if i == True:
        print("yes", end = " ") 
    else:
        print("no", end = " ") 
