
def solution(n, build_frame):
    answer = []
  
    for matetial in build_frame: 
        x,y , c_b ,  d_n = matetial
        
        #설치하려고 할 때
        if d_n ==1:
            #설치하려는 것이 기둥일 때 (0)
            answer.append([x,y,c_b])
            for check in answer:
                matetial_x,matetial_y,col_beam = check
                if col_beam == 0:
                    # 바닥이거나 아래에 기둥이 있거나 양쪽중 한 곳에 보가 있을 때 
                    if matetial_y == 0 or [matetial_x-1,matetial_y,1] in answer or [matetial_x,matetial_y,1] in answer or [matetial_x,matetial_y-1,0] in answer:
                        continue
                    else:
                        answer.remove([x,y,c_b])
                        break
                #설치하려는것이 보일 때 (1)
                else:
                    #양쪽중 한쪽아래에 기둥이 있거나 양 쪽에 보가 있을 때 
                    if[matetial_x,matetial_y-1,0] in answer or [matetial_x+1,matetial_y-1,0] in answer or ([matetial_x-1,matetial_y,1] in answer and [matetial_x+1,matetial_y,1] in answer):
                        continue
                    else:
                        answer.remove([x,y,c_b])
                        break
        #제거하려고 할 때 
        else:
            answer.remove([x,y,c_b])
            for check in answer:
                matetial_x,matetial_y,col_beam = check
                 #제거하려는 것이 기둥일 때 (0)
                if col_beam == 0:
                    #제거를 할 기둥위쪽이나 아래에  기둥이 없거나 양쪽에 보가 정상이거나 아무것도 없을 때 
                    if matetial_y == 0 or [matetial_x-1,matetial_y,1] in answer or [matetial_x,matetial_y,1] in answer or [matetial_x,matetial_y-1,0] in answer:
                        continue
                    else:
                        answer.append([x,y,c_b])
                        break
                #제거하는 것이 보일 때 (1)       
                else:
                    #제거를 했을 때 양쪽에 보들이 한쪽에 기둥이 받치고 있거나 제거한 보 아래에 기둥이 있을때
                    if [matetial_x,matetial_y-1,0] in answer or [matetial_x+1,matetial_y-1,0] in answer or ([matetial_x-1,matetial_y,1] in answer and [matetial_x+1,matetial_y,1] in answer):
                        continue
                    else:
                        answer.append([x,y,c_b])
                        break
        
    answer = sorted(answer,key=lambda x : (x[0],x[1],x[2]))
    return answer


n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n,build_frame))