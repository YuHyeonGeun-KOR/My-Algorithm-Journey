def solution(lottos, win_nums):
    answer = []

    hit_origin = 0
    hit_min = 0 
    hit_max= 0
    win = [6,6,5,4,3,2,1]
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            hit_origin +=1

    hit_max += hit_origin   
    hit_min = hit_origin
    for i in range(len(lottos)):
        if lottos[i] == 0:
            hit_max +=1
       
    answer = list((win[hit_max],win[hit_min]))
    return answer


lottos = [44, 1, 0, 0, 31, 25]	
win_nums = 	[31, 10, 45, 1, 6, 19]
print(solution(lottos,win_nums))