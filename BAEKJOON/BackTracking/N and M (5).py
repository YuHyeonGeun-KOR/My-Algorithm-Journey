import sys
input = sys.stdin.readline

n , m = map(int, input().split())
arr = list(map(int, input().split()))


def check(num_arr, length, visit_check) :
    global arr
    if len(num_arr) == length:
        for num in num_arr:
            print(num,end = " ")
        
        print("")
        return
    for i in range(n):
        if visit_check[i] != 1:
            visit_check[i] = 1
            num_arr.append(arr[i])
            check(num_arr , length , visit_check)
            visit_check[i] = 0
            num_arr.pop()
    return


arr = sorted(arr)
visited = [0] * len(arr)
answer = []
for i in range(n):
    visited[i] = 1
    answer.append(arr[i])
    check(answer , m,visited)
    answer.pop()
    visited[i] = 0