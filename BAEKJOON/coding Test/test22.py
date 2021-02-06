def solution(line):
    answer =[]
    x_list= []
    y_list = []
    for i in range(len(line)):
        for j in range(i,len(line)):
            try:
                x = (line[i][1]*line[j][2]) - (line[i][2] * line[j][1])  /(line[i][0]* line[j][1]) - (line[i][1] * line[j][0])   
                y = (line[i][2]*line[j][0]) - (line[i][0] * line[j][2])  /(line[i][0]* line[j][1]) - (line[i][1] * line[j][0]) 
                if int(x) == x and int(y) == y :
                    x_list.append(x)
                    y_list.append(y)
    return answer

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]

print(solution(line))