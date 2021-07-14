import sys
input = sys.stdin.readline

n,m = map(int, input().split())

rice = list(map(int, input().split()))

rice = sorted(rice)

def b_search(array, target, start, end):
    result = 0 
    while start < end:
        l = 0
        mid = (start + end) //2
        for i in range(len(array)):
            if array[i] <= mid:
                continue
            else:
                l += (array[i] - mid)
        if l >= target:
            start = mid +1
            result = mid
        else:
            end = mid - 1

    return result

print(b_search(rice, m, 0, rice[-1])) 