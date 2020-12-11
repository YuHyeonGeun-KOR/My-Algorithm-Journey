N = int(input())

parts = list(map(int, input().split()))

parts.sort()

M = int(input())

find = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid]  < target:
            start = mid +1
        else:
            end = mid - 1
    return None

for i in range(M):
    if binary_search(parts,find[i],0,N-1) == None:
        print('No',end= ' ')
    else :
        print('yes',end= ' ')



