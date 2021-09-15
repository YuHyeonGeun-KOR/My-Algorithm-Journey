import sys
input = sys.stdin.readline
n = int(input())

board = []

for i in range(n):
    board.append(list(input()))

def count (board,row,col):
    count =1
    result=1
    for i in range(row,len(board)):
        count =1
        for j in range(1,len(board)):
            if board[i][j] == board[i][j-1]:
                count +=1
            else:
                count =1
            result = max(count, result)
        

    for i in range(col,len(board)):
        count =1
        for j in range(1,len(board)):
            if board[j][i] == board[j-1][i]:
                count +=1   
            else:
                count =1
            result = max(count, result)
    return result

max_sum = 0
for i in range(n):
    for j in range(n):
        if j < n-1:
            board[i][j] , board[i][j+1]  = board[i][j+1] , board[i][j]
            max_sum = max(max_sum , count(board,i,j))
            board[i][j] , board[i][j+1]  = board[i][j+1] , board[i][j]
        
        if i < n-1:
            board[i][j] , board[i+1][j]  = board[i+1][j] , board[i][j]
            max_sum = max(max_sum , count(board,i,j))
            board[i][j] , board[i+1][j]  = board[i+1][j] , board[i][j]
        
             
print(max_sum)
