import sys
input = sys.stdin.readline

tooth = [[] for i in range(0,4)]
for i in range(0,4):
    ns =input().rstrip()
    for j in str(ns):
        tooth[i].append(j)
print(tooth)    


def rotate(tooth_n, r):
    if r == -1:
        tooth[tooth_n-1][0],tooth[tooth_n-1][1:7] = tooth[tooth_n-1][7],tooth[tooth_n-1][0:6]
    elif r == 1:
        tooth[tooth_n-1][7],tooth[tooth_n-1][0:6] = tooth[tooth_n-1][0],tooth[tooth_n-1][1:7]

def other_rotate(tooth_n, r):
    rotate = True
    if tooth_n == 1 and tooth[0][2] != tooth[1][6]:
        rotate(2, -1 *r )
        if tooth[1][2] != tooth[2][6]:  
            rotate(3,  r )
        else :
            rotate = False
            
        if tooth[2][2] != tooth[3][6]:  
            rotate(4, -1 * r )
    else :
        return 


    if tooth_n == 2 and tooth[1][6] != tooth[0][2]:
        rotate(1, -1 *r )
        if tooth[1][2] != tooth[2][6]:  
            rotate(3, -1 * r )
        if tooth[2][2] != tooth[3][6]:  
            rotate(4, r )
        
    if tooth_n == 3 and tooth[2][2] != tooth[3][6]:
        rotate(4, -1 *r )
        if tooth[2][6] != tooth[1][2]:  
            rotate(2, -1 * r )
        if tooth[2][2] != tooth[3][6]:  
            rotate(4, r )
        
    if tooth_n == 1 and tooth[0][2] != tooth[1][6]:
        rotate(2, -1 *r )
        if tooth[1][2] != tooth[2][6]:  
            rotate(3, -1 * r )
        if tooth[2][2] != tooth[3][6]:  
            rotate(4, -1 * r )
        


           

print(tooth)