import sys 

input = sys.stdin.readline

sys.setrecursionlimit(100000)

def dfs (start_x,start_y,w,h ):
    if start_x <= -1 or start_x  >= h or start_y <= -1 or start_y  >= w:
        return False

    if landBoard[start_x][start_y] == 1:
        landBoard[start_x][start_y] = 0
        dfs(start_x -1,start_y,w,h)
        dfs(start_x +1,start_y,w,h)
        dfs(start_x ,start_y +1,w,h)
        dfs(start_x ,start_y -1,w,h)
        dfs(start_x -1,start_y+1,w,h)
        dfs(start_x +1,start_y-1,w,h)
        dfs(start_x -1,start_y-1,w,h)
        dfs(start_x +1,start_y+1,w,h)
        return True
    
    return False
result = []
while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0 :
        break
    
    visited = [[0]*w for _ in range(h)]
    landBoard = []
    for i in range(h):
        landBoard.append(list(map(int, input().split())))

    count = 0
    
    
    for i in range(h):
        for j in range(w):
            if landBoard[i][j] == 1:
                if dfs(i,j,w,h) == True:
                    count +=1
    result.append(count)

for i in result:
    print(i)