import sys
input = sys.stdin.readline

def b_search(array , start , end ):
    while start <= end:
        mid = (start+end) //2
        
        if array[mid] > mid:
            end = mid -1
        elif array[mid] < mid:
            start = mid +1
        else:
            return mid
    return False
        

n = int(input())

array = list(map(int, input().split()))

result = b_search(array, 0, n)

if result == False:
    print(-1)
else:
    print(result)