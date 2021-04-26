from bisect import bisect_left ,bisect_right

n,x = map(int,input().rstrip().split())

num_list = list(map(int,input().rstrip().split()))

right_index = bisect_right(num_list,x)
left_index = bisect_left(num_list,x)
if right_index == n or left_index == n:
    print(-1)
else:
    print(right_index-left_index)


