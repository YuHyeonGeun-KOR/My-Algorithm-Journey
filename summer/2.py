from collections import deque
def solution(t, r):
    answer = []
    new = []
    for i in range(len(t)):
        new.append([t[i],r[i]])
    new = sorted(new, key = lambda x : (x[0],x[1]))
    new_que = deque(new)


    for i in range(len(new_que)-1):
        temp = new_que.popleft()
        temp2= new_que.popleft()
        if temp[0] == temp2[0]:
            temp2[0] += 1 
            answer.append(temp[1])
            new_que.appendleft(temp2)
        else:
            new_que.appendleft(temp)
            answer.append(temp2[1])
        new_que = sorted(new_que, key = lambda x : (x[0],x[1]))
        new_que = deque(new_que)
        
    temp = new_que.popleft()
    answer.append(temp[1])
    return answer

t =[7,6,8,5,5,5]
r= [0,1,2,3,4,5]
print(solution(t,r))