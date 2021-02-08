def solution(numbers, hand):
    answer = ''
    pad = {'1' : (0,0),'2' : (0,1),'3' : (0,2),
           '4' : (1,0),'5' : (1,1),'6' : (1,2),
           '7' : (2,0),'8' : (2,1),'9' : (2,2),
           '*' : (3,0),'0' : (3,1),'#' : (3,2)}
    left = '*'
    right = '#'
    for i in numbers:
        if i in [1,4,7]:
            left = str(i)
            answer = answer +'L'
        elif i in [3,6,9]:
            right = str(i)
            answer = answer + 'R'
        else:
            num = str(i)
            d_r = abs(pad[num][0] -  pad[right][0]) + abs(pad[num][1] -  pad[right][1]) 
            d_l = abs(pad[num][0] -  pad[left][0]) + abs(pad[num][1] -  pad[left][1])

            if d_l < d_r :
                left = str(i) 
                answer = answer +'L'    
            elif d_l > d_r :
                right = str(i) 
                answer = answer +'R'
            else:
                if hand == "right":
                    right = str(i)
                    answer = answer + 'R'
                elif hand == "left":
                    left = str(i)
                    answer = answer + 'L'    
            

              
    return answer


numbers =[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"

print(solution(numbers,hand))

