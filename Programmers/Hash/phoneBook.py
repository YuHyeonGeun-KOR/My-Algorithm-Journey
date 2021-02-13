def solution(phone_book):
    answer = True
    for i in phone_book:
        origin_list = list(i)
        for j in phone_book:
            if i != j :
                check_list = list(j)
                if check_list[0:len(origin_list)]== origin_list:
                    answer = False
                    return answer
    return answer