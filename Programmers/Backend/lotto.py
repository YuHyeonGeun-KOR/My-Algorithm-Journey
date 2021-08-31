def solution(lottos, win_nums):
    answer = []
    rank = [6,6,5,4,3,2,1]

    zero_count =0 
    correct_count= 0
    for lotto in lottos:
        if lotto in win_nums:
            correct_count +=1
            win_nums.remove(lotto)

        if lotto == 0:
            zero_count +=1

    min_count = correct_count
    max_count = correct_count + zero_count

    answer = [rank[max_count] , rank[min_count]]

    return answer


lottos = [44, 1, 0, 0, 31, 25]
win_nums = 	[31, 10, 45, 1, 6, 19]
print(solution(lottos,win_nums))