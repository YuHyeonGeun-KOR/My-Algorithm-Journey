def solution(n, build_frame):
    answer = []

    for work in build_frame:
       
        x,y,col_or_beams,do_or_not = work
        T_F = True
        if do_or_not == 1:
            answer.append([x,y,col_or_beams])
            for check in answer:
                check_x,check_y,check_c_o_b = check
                if check_c_o_b == 0:
                    if check_y == 0 or [check_x-1,check_y,1] in answer or [check_x,check_y,1] in answer or [check_x,check_y-1,0] in answer:
                        continue
                    else:
                        T_F = False
                        break
                elif check_c_o_b == 1:
                    if [check_x,check_y-1,0] in answer or [check_x+1,check_y-1,0] in answer or ([check_x-1,check_y,1] in answer and [check_x+1,check_y,1] in answer):
                        continue
                    else:
                        T_F = False
                        break
            if T_F == False:
                answer.remove([x,y,col_or_beams])
                
        elif do_or_not == 0:
            answer.remove([x,y,col_or_beams])
            for check in answer:
                check_x,check_y,check_c_o_b = check
                if check_c_o_b == 0:
                    if check_y == 0 or [check_x-1,check_y,1] in answer or [check_x,check_y,1] in answer or [check_x,check_y-1,0] in answer:
                        continue
                    else:
                        T_F = False
                        break
                elif check_c_o_b == 1:
                    if [check_x,check_y-1,0] in answer or [check_x+1,check_y-1,0] in answer or ([check_x-1,check_y,1] in answer and [check_x+1,check_y,1] in answer):
                        continue
                    else:
                        T_F = False
                        break
            if T_F == False:
                answer.append([x,y,col_or_beams])
    
    return sorted(answer)


n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n,build_frame))