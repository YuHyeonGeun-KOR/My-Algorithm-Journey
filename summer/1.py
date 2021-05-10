def solution(code, day, data):
    answer = []
    new_data = sorted(data, key = lambda x :x[-10:])
    c = "code="
    t = "time="
    c += code
    t += day
    for i in new_data:
        if c in i and t in i:
            new = i
            new = new.split()
            p = new[0].replace("price=","")
            answer.append(int(p))
    return answer

data = ["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]
print(solution("012345","20190620",data))