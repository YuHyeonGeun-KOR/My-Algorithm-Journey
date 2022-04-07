from collections import deque
def solution(n, k, cmd):
    answer = ["O"] * n
    index = k
    d_list = []
    for i in range(n):
        d_list.append([-1+i,i+1])
    d_list[-1][1] = -1
    trash = deque()
    for c in cmd:
        if len(c)>=2:
            command , idx  = c.split(" ")
        else:
            command = c
        if command == "D":
            for i in range(int(idx)):
                index = d_list[index][1]
        elif command == "U":
            for i in range(int(idx)):
                index = d_list[index][0]  
        elif command == "C":
            trash.appendleft([index ,d_list[index]])
            if d_list[index][0] == -1:
                d_list[d_list[index][1]][0] = -1
                index = d_list[index][1]
            elif d_list[index][1] == -1:
                d_list[d_list[index][0]][1] = -1
                index = d_list[index][0]
            else:
                d_list[d_list[index][1]][0] = d_list[index][0]
                d_list[d_list[index][0]][1] = d_list[index][1]
                index = d_list[index][1]
        elif command == "Z":
            restore = trash.popleft()
            if restore[1][0] == -1:
                d_list[restore[1][1]][0] = restore[0]
            elif restore[1][1] == -1:
                d_list[restore[1][0]][1] = restore[0]
            else:
                d_list[restore[1][0]][1] = restore[0]
                d_list[restore[1][1]][0] = restore[0]
            
    for t in trash:
        answer[t[0]] = "X"    
    return "".join(answer)

print(solution(8,2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))