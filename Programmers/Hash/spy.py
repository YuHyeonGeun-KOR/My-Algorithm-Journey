def solution(clothes):
    answer = 1
    c = {}
    for i in clothes:
        try : c[i[1]] += 1
        except : c[i[1]] = 1

    print(c)

    for wear, count in c.items():
        answer *= (count+1)

    return answer - 1