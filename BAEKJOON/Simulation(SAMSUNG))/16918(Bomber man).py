
Bomb_x = [1,-1,0,0]
Bomb_y = [0,0,1,-1]

r,c,n = map(int,input().split())
board = []
check = [[0]*c for o in range(r)]

for i in range(0,r):
    board.append(list(input()))

def show_print(board):            
    for i in range(0,r):
        board[i] = "".join(board[i])
        print(board[i])

def Bomb_check(board,check):
    m_check = [[0]*c for o in range(r)]
    for i in range(0,r):
        for j in range(0,c):
            if board[i][j] == "O":
                m_check[i][j] = 1
    return m_check

def Bomb_Bomb(check):
    M_board = [["O"] * c for _ in range(r)] 
    for i in range(0,r):
        for j in range(0,c):
            if check[i][j] == 1:
                M_board[i][j] ="." 
                for k in range(0,4):
                    if 0<= i+Bomb_x[k]  <r and 0 <= j+Bomb_y[k] <c:
                        M_board[i+Bomb_x[k]][j+Bomb_y[k]] = "." 
    
    return M_board

def Make_Board():
    m_board = [["O"] * c for _ in range(r)] 
    return m_board


for i in range(1,n+1):
    if i == 1:
        check = Bomb_check(board,check)
    elif i % 2 == 0:
        board = Make_Board()
    else :
        board = Bomb_Bomb(check)        
        check =Bomb_check(board,check)

for i in range(r):
    board[i] = "".join(board[i])
    print(board[i])