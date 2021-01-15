import sys
input = sys.stdin.readline

N= int(input())

A = list(map(int, input().split()))

M = int(input())

B = list(map(int, input().split()))

A.sort()


def bst(array , target, start , end):
    while start <= end :
        mid = (start + end) // 2
        if target == array[mid]:
            return 1
        elif target < array[mid]:
            end = mid -1
        else :
            start = mid + 1
    return 0


for i in B:
    print(bst(A, i, 0, N-1))
