import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

m = int(input())

b = list(map(int, input().split()))

a.sort()
def bst(array, target, start, end):
    result = 0
    while start <= end:
        mid  = (start + end) // 2
       
        if target == array[start]:
            result += 1
            start = start + 1
            continue
        elif target == array[end]:
            result += 1    
            end = end - 1
            continue
        else :
            start = start + 1
            continue
        
        if target <= array[mid]:
            end = mid -1
        else :
            start = mid + 1

    
    return  result

for i in b:
    print(bst(a, i, 0, n-1) , end = " ")


