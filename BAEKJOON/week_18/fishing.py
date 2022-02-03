import sys
input = sys.stdin.readline

def catch (index,r,c):
    global board
    global sharks
    size =0 
    for i in range(r):
        if board[i][index]  != 0:
            size = board[i][index][2]
            board[i][index] = 0
            del sharks[sharks.index([i,index])]
            return size
    return 0

def shark_moving(r,c):
    global sharks
    global board
    new_sharks = []
    for shark in sharks:
        s,d,z = board[shark[0]][shark[1]]
        temp_s = s
        while temp_s !=0:
            if d == 1:
                shark[0] -=1
                if shark[0] < 0:
                    shark[0] =1
                    d = 2   
            elif d == 2:
                shark[0] +=1
                if shark[0] >= r:
                    shark[0] = r-2
                    d = 1
            elif d == 3:
                shark[1] +=1
                if shark[1] >= c:
                    shark[1] = c-2
                    d = 4
            elif d == 4:
                shark[1] -=1
                if shark[1] < 0:
                    shark[1] =1
                    d = 3
            

            temp_s -= 1
        new_sharks.append([shark[0], shark[1] ,s,d,z])
    new_sharks = sorted(new_sharks , key = lambda x : -1*x[4])
    sharks = []
    new_board = [[0]*(c) for _ in range(r)]
    for shark in new_sharks:
        if new_board[shark[0]][shark[1]] == 0:
            new_board[shark[0]][shark[1]] = [shark[2],shark[3],shark[4]]
            sharks.append([shark[0],shark[1]])

    board = new_board
    return


dx = [0,-1,1,0,0]
dy = [0,0,0,1,-1]
r,c,m = map(int, input().split())

board = [[0]*(c) for _ in range(r)]
sharks = []

for i in range(m):
    s_r, s_c, s, d ,z = map(int, input().split())
    sharks.append([s_r-1,s_c-1])
    board[s_r-1][s_c-1] = [s,d,z]

result  = 0
for i in range(c):
    
    result += catch(i,r,c) 
    if len(sharks) == 0:
        break
    shark_moving(r,c)
    

print(result)