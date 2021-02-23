from itertools import combinations

def solution(orders, course):
    answer = []
    course_candi = {}
    count = [0] * 11
    s=""
    for i in orders:
        for j in range(len(i)):
            c = list(combinations(i,j+1))
            for k in c:
                c.sort()
                if k not in course_candi:
                    course_candi[k] = 1
                else:
                    course_candi[k] +=1
    for i in course:
        for j in course_candi:
            if i == len(j) and course_candi[j] >= count[len(j)]  and course_candi[j] > 1:
                count[len(j)] = course_candi[j]
    for i in course:
        for j in course_candi:
            s=""
            if i == len(j) and course_candi[j] == count[len(j)]  and course_candi[j] > 1:
                s ="".join(sorted(j))
                answer.append(s)
    
    
    answer = list(set(answer))                        
    answer.sort()
    return answer


orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
solution(orders, course)