from collections import deque
def checker(i,j,board):
    checkList = []

    checkList.append(board[i][j])
    checkList.append(board[i][j+1])
    checkList.append(board[i+1][j])
    checkList.append(board[i+1][j+1])

    if len(set(checkList)) == 1:
        return True

def delete (i, j, board):
    count = 0
    queue = deque()
    queue.append([i,j])
    start = board[i][j]
    visited = [[0] * len(board[0]) for _ in range(len(board))]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    while queue:
        now = queue.popleft()
        print(now)
        x , y = now[0], now[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < len(board) and 0<= ny < len(board):
                if visited[nx][ny] == 0 and board[nx][ny] == start:
                    count +=1 
                    visited[nx][ny] = 1
                    board[nx][ny] = 0 
                    queue.append([nx,ny])
        

        for i in range(1, len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0 and board[i-1][j] != 0 :
                    board[i][j] = board[i-1][j]

    return count , board

                    


    
def solution(m, n, board):
    answer = 0

    for i in range(m-2):
        for j in range(n-2):
            if checker(i,j,board):
                count , board = delete(i,j,board)
                answer += count



    return answer

board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

print(solution(4,5, board))