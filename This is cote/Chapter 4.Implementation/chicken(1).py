from itertools import combinations
import sys
input = sys.stdin.readline
n,m = map(int, input().split())

board = []
house = []
chicken = []
Big_Chicken = []
result = []
for i in range(n):
    board.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append([i,j])
        elif board[i][j] == 2:
            chicken.append((i,j))



Big_Chicken = list(combinations(chicken,m))


for i in Big_Chicken:
    m_list = []

    for j in house:
        x = j[0]
        y = j[1]
        distance = 50000
        for k in i:
            distance = min(distance,abs(x - k[0]) + abs(y - k[1]))
         
        
        m_list.append(distance)
            
    result.append(sum(m_list))
    
print(min(result))