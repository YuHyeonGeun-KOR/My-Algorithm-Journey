def solution(board, moves):
    answer = 0
    moved=[0]  
    for i in moves:
        i-=1
        for j in range(len(board)):
            if board[j][i] !=0:   
                moved.append(board[j][i]) 
                board[j][i]=0  
                if moved[-1] == moved[-2]:                
                    moved.pop(-1)    
                    moved.pop(-1)
                    answer+=2 
                break  
    
            
    return answer