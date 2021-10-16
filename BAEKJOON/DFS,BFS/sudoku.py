import sys
input =sys.stdin.readline

sudoku_board = []
for i in range(9):
    sudoku_board.append(list(map(int, input().split())))


test_postion = []

for i in range(9):
    for j in range(9):
        if sudoku_board[i][j] == 0:
            test_postion.append((i,j))


def candi_num (i, j):
    all_num = [1,2,3,4,5,6,7,8,9]

    for k in range(9):
        if sudoku_board[k][j] in all_num:
            all_num.remove(sudoku_board[k][j])
        if sudoku_board[i][k] in all_num:
            all_num.remove(sudoku_board[i][k])

    i = i//3
    j = j//3

    for r in range(i * 3 , i*3 + 3):
        for c in range(j * 3, j *3 + 3):
            if sudoku_board[r][c]  in all_num:
                all_num.remove(sudoku_board[r][c])

    return all_num

finish_falg = False

def dfs(n):
    global finish_falg
    if finish_falg:
        return 

    if n == len(test_postion):
        for row in sudoku_board:
            print(*row)
        finish_falg = True
        return 
    else:
        i, j = test_postion[n]
        input_num = candi_num(i,j)
        for i_n in input_num:
            sudoku_board[i][j] =  i_n
            dfs(n+1)
            sudoku_board[i][j] =  0
        
dfs(0)



