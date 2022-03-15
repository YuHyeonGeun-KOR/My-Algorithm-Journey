def solution(rows, columns, queries):
    answer = []
    board = [[0]*columns for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = num
            num +=1
            
    for q in queries:
        x1 , y1, x2, y2 = q[0], q[1] , q[2] , q[3]
        num_list = []
        x = x1-1 
        y = y1-1
        for _ in range(y2-y1):
            num_list.append(board[x][y])
            y+=1
        for _ in range(x2-x1):
            num_list.append(board[x][y])
            x+=1
        for _ in range(y2-y1):
            num_list.append(board[x][y])
            y-=1
        for _ in range(x2-x1):
            num_list.append(board[x][y])
            x-=1
        
        answer.append(min(num_list))
        
        index = 0 
        for i in range(y1, y2):
            board[x1-1][i] = num_list[index]
            index +=1
        for i in range(x1,x2):
            board[i][y2-1] = num_list[index]
            index +=1
        for i in range(y2-2 , y1-1 , -1):
            board[x2-1][i] = num_list[index]
            index +=1
        for i in range(x2-1 , x1-1 , -1):
            board[i][y1-1] = num_list[index]
            index +=1
        board[x1-1][y1-1] = num_list[index]
    return answer