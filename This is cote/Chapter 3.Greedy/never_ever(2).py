import sys
input = sys.stdin.readline

N = int(input())
coin = list(map(int, input().split()))

target  = 1
coin.sort()
for i in coin:
    if target < i:
        break
    target += i

print(target)
    