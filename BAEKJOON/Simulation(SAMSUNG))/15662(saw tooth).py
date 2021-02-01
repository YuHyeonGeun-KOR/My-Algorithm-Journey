from collections import deque
n = int(input())
List = []
for i in range(0,n):
    List.append(deque(map(int, input())) )


check = []
result = 0
def other_rotate(tooth_n, r):
    now = tooth_n-1
        
    while(now >= 1) :
        if List[now][6]!= List[now-1][2]:
            check[now-1] = check[now]*(-1)
            now -=1
        else:
            break 

    while(now < n-1) :
        if List[now][2]!= List[now+1][6]:
            check[now+1] = check[now]*(-1)
            now +=1
        else:
            break 

    return

k = int(input())

for i in range(0,k):
    saw_num , clock = map(int,input().split())
    check = [0] * n 
    check[saw_num-1] = clock           
    other_rotate(saw_num,clock)
    for j in range(0,n):
        List[j].rotate(check[j])
    

for i in range(0,n):
    if List[i][0] == 1:
        result += 1
print(result)    

