from collections import deque

tooth_1 = deque(map(int, input())) 
tooth_2 = deque(map(int, input())) 
tooth_3 = deque(map(int, input())) 
tooth_4 = deque(map(int, input()))



def other_rotate(tooth_n, r):
        
    if tooth_n == 1 :
        if tooth_1[2] != tooth_2[6]:
            if tooth_2[2] != tooth_3[6]:      
                if tooth_3[2] != tooth_4[6]:  
                    tooth_4.rotate(-r)
                tooth_3.rotate(r)    
            tooth_2.rotate(-r)  
        tooth_1.rotate(r)    


    if tooth_n == 2 :
        if tooth_2[6] != tooth_1[2]:
            tooth_1.rotate(-r)
        if tooth_2[2] != tooth_3[6]:  
            if tooth_3[2] != tooth_4[6]:  
                tooth_4.rotate(r)
            tooth_3.rotate(-r)
        tooth_2.rotate(r)   

    if tooth_n == 3 :
        if tooth_3[2] != tooth_4[6]:
            tooth_4.rotate(-r)
        if tooth_3[6] != tooth_2[2]:  
            if tooth_2[6] != tooth_1[2]:  
                tooth_1.rotate(r)
            tooth_2.rotate(-r)
        tooth_3.rotate(r)   
    if tooth_n == 4 :
        if tooth_4[6] != tooth_3[2]:
            if tooth_2[2] != tooth_3[6]:  
                if tooth_1[2] != tooth_2[6]:  
                    tooth_1.rotate(-r)
                tooth_2.rotate(r)    
            tooth_3.rotate(-r)
        tooth_4.rotate(r)   

    return

k = int(input())
for i in range(0,k):
    saw_num , clock = map(int,input().split())
    other_rotate(saw_num,clock)           

def solve ():
    r_sum = 0
    if tooth_1[0] == 1:
        r_sum += 1
    if tooth_2[0] == 1:
        r_sum += 2
    if tooth_3[0] == 1:
        r_sum += 4
    if tooth_4[0] == 1:
        r_sum += 8
    return r_sum

print(solve())


