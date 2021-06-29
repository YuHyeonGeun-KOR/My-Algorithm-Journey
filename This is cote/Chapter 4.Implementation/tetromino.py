import sys
input = sys.stdin.readline

N,M = map(int,input().split())

def illzza (N,M,board):
    result = 0
    for i in range(0,N):
        for j in range(0,M-3):
            result = max(result,sum(board[i][j:j+4]))
    
    for i in range(0,N-3):
        for j in range(0,M):
            result = max(result,(board[i][j]+board[i+1][j]+board[i+2][j]+board[i+3][j]))
    
    return result

def Nemo (N,M,board):
    result = 0
    for i in range(0,N-1):
        for j in range(0,M-1):
            result = max(result,sum(board[i][j:j+2])+sum(board[i+1][j:j+2]))
    
    return result

def Nieun (N,M,board):
    result = 0
    for i in range(0,N-2):
        for j in range(0,M-1):
            result = max(result,(board[i][j]+board[i+1][j]+board[i+2][j]+board[i+2][j+1]) , (board[i][j+1]+board[i][j]+board[i+1][j]+board[i+2][j]))
    
    for i in range(0,N-2):
        for j in range(1,M):
            result = max(result,(board[i][j]+board[i+1][j]+board[i+2][j]+board[i+2][j-1]),(board[i][j]+board[i+1][j]+board[i+2][j]+board[i][j-1]))
    

    for i in range(1,N):
        for j in range(0,M-2):
            result = max(result,(board[i][j]+board[i][j+1]+board[i][j+2]+board[i-1][j+2]),(board[i-1][j]+board[i][j]+board[i][j+1]+board[i][j+2]))

    for i in range(0,N-1):
        for j in range(0,M-2):
            result = max(result,(board[i][j]+board[i][j+1]+board[i][j+2]+board[i+1][j+2]),(board[i+1][j]+board[i][j]+board[i][j+1]+board[i][j+2]))   

    
    return result

def Rieul (N,M,board):
    result = 0
    for i in range(1,N-1):
        for j in range(0,M-1):
            result = max(result,(sum(board[i][j:j+2])+board[i-1][j]+board[i+1][j+1]),(sum(board[i][j:j+2])+board[i+1][j]+board[i-1][j+1]))
    
    for i in range(1,N):
        for j in range(1,M-1):
            result = max(result,(sum(board[i][j:j+2])+sum(board[i-1][j-1:j+1])),(sum(board[i-1][j:j+2])+sum(board[i][j-1:j+1])))
    
    return result
def Wu (N,M,board):
    result = 0
    for i in range(1,N-1):
        for j in range(1,M-1):
            result = max(result,(sum(board[i-1][j-1:j+2])+board[i][j]),(sum(board[i+1][j-1:j+2])+board[i][j]))
    
    for i in range(1,N-1):
        for j in range(1,M-1):
            result = max(result,(board[i-1][j-1]+board[i][j-1]+board[i+1][j-1]+board[i][j]),(board[i-1][j+1]+board[i][j+1]+board[i+1][j+1]+board[i][j]))
    
    for i in range(1,N-1):
        for j in range(1,M-1):
            result = max(result,(sum(board[i][j-1:j+2])+board[i-1][j]),(sum(board[i][j-1:j+2])+board[i+1][j]))
    for i in range(1,N-1):
        for j in range(1,M-1):
            result = max(result,(board[i-1][j]+board[i][j]+board[i+1][j]+board[i][j+1]),(board[i-1][j]+board[i][j]+board[i+1][j]+board[i][j-1]))
    return result
board = []
for i in range(N):
    board.append(list(map(int,input().split())))

print(max(illzza(N,M,board),Nemo(N,M,board),Nieun(N,M,board),Rieul(N,M,board),Wu(N,M,board)))
