import sys
from collections import deque
import copy
input = sys.stdin.readline

fire_meta = {}
fire_count = {}
dx = [-1, -1, 0, 1, 1,  1,  0, -1]
dy = [0 ,  1, 1, 1, 0, -1, -1, -1]
def move(x,y,meta,N):
    
    nx = x
    ny = y
   
    while meta:
        met = meta.popleft()
        fire_meta[(nx,ny)].popleft()
        m , s , d = met[0] , met[1] , met[2]
        x = (nx + s * dx[d]) % N 
        y = (ny + s * dy[d]) % N
        if (x,y) not in fire_meta:
            fire_meta[(x,y)] = deque([[m,s,d]])
        else:
            fire_meta[(x,y)].append([m,s,d])

    if len(fire_meta[(nx,ny)]) == 0:
        fire_meta.pop((nx,ny))        

    return
def divide (candi):
    while candi:
        index = candi.popleft()
        x , y = index[0] , index[1]

        count = len(fire_meta[(x,y)])
        odd_even_Flag = False
        m_sum = 0
        s_sum = 0 
        evencount = 0 
        oddcount = 0 
        for _ in range(count):
            now = fire_meta[(x,y)].popleft()
            m_sum += now[0]
            s_sum += now[1]
            if now[2] % 2  == 1 :
                oddcount +=1
            else:
                evencount +=1

        if oddcount == count or evencount == count:
            odd_even_Flag = True
        
        if m_sum//5 == 0 :
            fire_meta.pop((x,y))
        else:
            m_div = m_sum //5
            s_div = s_sum // count
            if odd_even_Flag :
                fire_meta[(x,y)].append([m_div ,s_div ,0])
                fire_meta[(x,y)].append([m_div ,s_div ,2])
                fire_meta[(x,y)].append([m_div ,s_div ,4])
                fire_meta[(x,y)].append([m_div ,s_div ,6])
            else:
                fire_meta[(x,y)].append([m_div ,s_div ,1])
                fire_meta[(x,y)].append([m_div ,s_div ,3])
                fire_meta[(x,y)].append([m_div ,s_div ,5])
                fire_meta[(x,y)].append([m_div ,s_div ,7])
    return 

N,M,K = map(int, input().split())

for i in range(M):
    r,c,m,s,d = map(int, input().split())
    fire_meta[(r,c)] = deque([[m,s,d]])

for _ in range(K):
    f_copy = copy.deepcopy(fire_meta)
    for key, value in f_copy.items():
        x , y =key[0] ,key[1]
        move(x,y,value ,N)  
    
    div_candi = deque([])
    f_copy = copy.deepcopy(fire_meta)
    for key ,value in f_copy.items():
        if len(value) >= 2:
            div_candi.append(key)
    divide(div_candi)     
                

        

result = 0 
for key, value in fire_meta.items():
    for meta in value:
        result += meta[0]

print(result)
