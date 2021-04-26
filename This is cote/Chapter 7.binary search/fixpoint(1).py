from collections import deque
n= int(input())

num_list = list(map(int, input().split()))

def binary_search(array,start,end):
    while True:
        if start > end:
            return -1
        mid = (start + end)//2
        if mid == num_list[mid] :
            return mid
        elif mid > num_list[mid]:
            start = mid + 1
        else:
            end  = mid-1   


print(binary_search(num_list,0,len(num_list)))
