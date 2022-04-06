
def find(money , number):
    if parent[number] == number or money == 0 :
        answer[number] += money
        return 
    not_mine = money // 10
    mine = money - not_mine
    answer[number] += mine
    find(not_mine , parent[number])
    return
def solution(enroll, referral, seller, amount):
    global answer
    answer = []
    global parent
    n = len(enroll)
    name_num = {}
    parent = [0] * (n+1)
    for i in range(1, n+1):
        parent[i] = i
    for i in range(n):
        name_num[enroll[i]] = i + 1
    for i in range(n):
        if referral[i] == "-":  # 민호가 추천인
            parent[i + 1] = 0
        else:
            parent[i + 1] = name_num[referral[i]]
    for i in range(len(seller)):
        find(amount[i] * 100, name_num[seller[i]])
    return answer

