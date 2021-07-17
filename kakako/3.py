def solution(n, k, cmd):
    answer = ''
    name = {}
    alpha = "A"
    for i in range(n):
        name[i] = chr(ord(alpha))
        alpha = chr(ord(alpha)+1)

    name_copy = name.copy()
    
    
    index = k

    cmd_list = []
    for i in cmd:
        s = i.replace(" ","")
        cmd_list.append(list(s))

    latest_del = []

    for i in cmd_list:
        if i[0] == "U":
            index -= int(i[1])
        elif i[0] == "D":
            index += int(i[1])
        elif i[0] == "C":
            if index == len(name_copy):
                latest_del.append([index , name_copy[index]])
                del name_copy[index]
                index -= 1
            else:
                latest_del.append([index , name_copy[index]])
                del name_copy[index]
                for j in range(index,len(name_copy)):
                    name_copy[j] = name_copy.pop(j+1)

        elif i[0] == "Z":
            z_index , z_name = latest_del.pop(-1)
            if z_index in name_copy:
                temp_name = name_copy.pop(z_index)
                name_copy[z_index] = z_name
                for j in range(len(name_copy)-1,z_index,-1):
                    name_copy[j+1] = name_copy.pop(j)
                name_copy[z_index+1]  = temp_name
            else:
                name_copy[z_index] = z_name
    
    name_copy = {x: y for y, x in name_copy.items()}
    
    for key, value in name.items():
        if value in name_copy:
            answer += "O"
        else:
            answer += "X"
    return answer



n=8
k=2
cmd =["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmd))