import sys
from collections import deque
input = sys.stdin.readline

fire_meta = {}
fire_count = {}

def move(x,y,meta,N):
    nx = x
    ny = y
    while meta:
        x = nx
        y = ny
        met = meta.popleft()
        m , s , d = met[0] , met[1] , met[2]
        fire_count[(nx,ny)] -=1
        if d == 1 or d == 0 or d == 7:
            for i in range(s):
                x-=1
                if x == 0:
                    x = N
        elif d == 5 or d == 4 or d == 3:
            for i in range(s):
                x+=1
                if x == N+1:
                    x = 1
        
        if d == 1 or d == 2 or d == 3:
            for i in range(s):
                y += 1
                if y == N+1:
                    y = 1
        elif d == 7 or d == 6 or d == 5:
            for i in range(s):
                y -= 1
                if y == 0 :
                    y = N

        if (x,y) not in fire_count:
            fire_count[(x,y)] = 1
        else:
            fire_count[(x,y)] += 1

        if (x,y) not in fire_meta:
            fire_meta[(x,y)] = deque([[m,s,d]])
        else:
            fire_meta[(x,y)].append([m,s,d])

        if len(fire_meta[(nx,ny)]) == 0  :
            fire_meta.pop((nx,ny))
            fire_count.pop((nx,ny))

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
            fire_count.pop((x,y))
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
            fire_count[(x,y)] = 4
    return 

N,M,K = map(int, input().split())

for i in range(M):
    r,c,m,s,d = map(int, input().split())
    fire_meta[(r,c)] = deque([[m,s,d]])
    fire_count[(r,c)] = 1

for _ in range(K):
    fire_meta_copy = fire_meta.copy()
    for key, value in fire_meta_copy.items():
        x , y =key[0] ,key[1]
        move(x,y,value ,N)

    
    div_candi = deque([])
    fire_count_copy = fire_count.copy()
    for key ,value in fire_count_copy.items():
        if value >= 2:
            div_candi.append(key)

    divide(div_candi)
                
                

        

result = 0 
for key, value in fire_meta.items():
    for meta in value:
        result += meta[0]

print(result)
