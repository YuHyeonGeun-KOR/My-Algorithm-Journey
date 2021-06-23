import sys
input = sys.stdin.readline

N,M,K = map(int, input().split())

array  = list(map(int, input().split()))

array.sort(reverse=True)
result_0 = (M//K) * K * array[0]
result_1 = (M - (M//K) * K) * array[1]

print(result_0,result_1)
print(result_0+result_1)