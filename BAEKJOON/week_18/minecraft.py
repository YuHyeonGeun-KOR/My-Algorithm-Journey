import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

height = 0
ans = 1e9

for i in range(257):
    over_block = 0
    lower_block = 0
    for j in range(n):
        for k in range(m):
            if board[j][k] < i:
                lower_block += (i - board[j][k])
            else:
                over_block += (board[j][k] - i)
    bag = over_block + b
    if bag < lower_block:
        continue
    time = 2 * over_block + lower_block
    if time <= ans:
        ans = time
        height = i
print(ans, height)