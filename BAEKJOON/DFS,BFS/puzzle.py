import sys
from collections import deque
input = sys.stdin.readline

board = []
for i in range(3):
    board.append(list(map(int, input().split())))


def find_zero(board) :
    for i in range(3):
        for j in range(3):
            if board[i][j] == '0' or board[i][j] == 0:
                return [i,j]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def list_2_to_one (board):
    l = ""
    for i in range(3):
        for j in range(3):
            l += str(board[i][j])
    return l

def list_1_to_2(l):
    new = [[],[],[]]
    for i in range(3):
        for j in range(3):
            new[i].append(l[3*i + j])
    return new

queue = deque()
visited = set()
visited.add(list_2_to_one(board))
cnt = 0
answer = -1
start = [0,list_2_to_one(board)]
queue.append(start)

target = "123456780"
while queue:
    cnt, l = queue.popleft()

    if l == target:
        answer = cnt
        break
    check_board = list_1_to_2(l)
    zero = find_zero(check_board)
    for i in range(4):
        xx = zero[0] + dx[i]
        yy = zero[1] + dy[i]

        if 0<= xx < 3 and 0 <= yy <3:
            check_board[zero[0]][zero[1]] , check_board[xx][yy] = check_board[xx][yy] , check_board[zero[0]][zero[1]]
            l = list_2_to_one(check_board)
            if l not in visited:
                visited.add(l)
                queue.append([cnt + 1, l])
            check_board[zero[0]][zero[1]] , check_board[xx][yy] = check_board[xx][yy] , check_board[zero[0]][zero[1]]

print(answer)
