n,m = map(int,input().split())
card = [list(map(int,input().split())) for i in range(n)]

print(card)

lowest_N = card[0][0]
col = 0
row = 0

for i in range(n):
    if card[i][0] <= lowest_N:
        lowest_N =  card[i][0]
        row = i


lowest_M = card[row][0]

for j in range(m):
    if card[row][j]<=lowest_M:
        lowest_N = card[row][j]

print(lowest_M)