import copy
from collections import deque
def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]

def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]

def rotate90(arr):
    return list(zip(*arr[::-1]))

def dfs_counter (x,y,width,area_copy):
    
    queue = deque()
    queue.append((x,y))
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while queue:
        x,y=queue.popleft()

        for i in range (4):
            xx = x + dx[i]
            yy = y + dy[i]

            if xx <= -1 or xx >= width or yy <= -1 or yy >= width:
                continue 
            elif area_copy[xx][yy]==0:
                area_copy[xx][yy] = area_copy[x][y] +1
                queue.append((xx,yy))
            elif area_copy[xx][yy]==0:
                continue
    return area_copy


def dfs_shape (x,y,width,temp_shape,area_copy):
    
    queue = deque()
    queue.append((x,y))
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    temp_shape.append([x,y])
    while queue:
        x,y=queue.popleft()
        if [x,y]not in temp_shape:
            temp_shape.append([x,y])
        for i in range (4):
            xx = x + dx[i]
            yy = y + dy[i]

            if xx <= -1 or xx >= width or yy <= -1 or yy >= width:
                continue 
            elif area_copy[xx][yy]==1:
                area_copy[xx][yy] = area_copy[x][y] -1
                queue.append((xx,yy))
                
            elif area_copy[xx][yy]==0:
                continue
    
    return temp_shape

    
    
def solution(game_board, table):
    
    answer = []
    width = len(game_board)
    empty_cnt = 0
    shape_array = []
    result_cnt = 0
    board_copy = copy.deepcopy(game_board)
    table_copy = copy.deepcopy(table)
    for i in range(width):
        for j in range(width):
            if board_copy[i][j] == 0:
                dfs_counter(i,j,width,board_copy)
                empty_cnt += 1
    
    for i in range(width):
        for j in range(width):
            if table_copy[i][j] == 1:
                temp_shape = []
                shape_array.append(dfs_shape(i,j,width,temp_shape,table_copy))


    new_board = [[1] * (width*2+6) for _ in range(width*2+6)]
    
    for i in range(width):
        for j in range(width):
            new_board[width+i][width+j] = game_board[i][j]
    
    
    for shape in shape_array:
        
        key = [[0] * (width) for _ in range(width)]
        
        for i in shape:
            key[i[0]][i[1]] += 1
        
        rotated_key = key
        break_flag = True
        for _ in range(4):
            rotated_key = rotate90(rotated_key)
            if break_flag == False:
                    break
            for x in range(1, 6+width):
                if break_flag == False:
                    break
                for y in range(1,6+width):
                    if break_flag == False:
                        break
                    
                    attach(x, y, width, rotated_key, new_board)
                    
                    ifGoingRight = True


                    for check_board in new_board:
                        if 2 in check_board:
                            detach(x, y, width, rotated_key, new_board)    
                            ifGoingRight = False
                            break
                    if not ifGoingRight:
                        continue 
                   

                    newBoard_copy = copy.deepcopy([row[width:width+width] for row in new_board[width:width+width]])
                   
                    
                    new_empty_cnt = 0
                    for check_x in range(width):
                        for check_y in range(width):
                            if newBoard_copy[check_x][check_y] == 0:
                                dfs_counter(check_x,check_y,width,newBoard_copy)
                                new_empty_cnt += 1
                    

                    if new_empty_cnt == empty_cnt-1:
                        result_cnt += len(shape)
                        empty_cnt -=1
                        break_flag = False
                    else:
                        detach(x, y, width, rotated_key, new_board)        
            
            
                        

    answer.append(result_cnt)
    return answer[0]


game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = 	[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

print(solution(game_board, table))