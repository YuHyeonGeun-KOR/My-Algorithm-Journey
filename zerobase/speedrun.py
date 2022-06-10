
def fight(idx , power , reward, health , optional ,time ,  result):
    print(idx , power , reward, health , optional ,time ,  result)
    if idx == len(reward) and set(optional) :
        result.append(time)
        return 
    if optional[idx] == 1:
        if health[idx] - power > 0:
            health[idx] -= power
            fight(idx , power , reward, health , optional ,time + 1,  result)
            health[idx] += power
        else:
            health[idx] -= power
            fight(idx + 1 , power+reward[idx] , reward, health , optional ,time + 1,  result)
            health[idx] += power
    else:
        optional[idx] = 1
        fight(idx , power , reward, health , optional ,time,  result)
        fight(idx+1 , power , reward, health , optional ,time,  result)


    return

def solution(reward, health, optional):
    answer = 0
    result = []
    answer  = fight(0 , 1 , reward, health , optional , 0  ,result)
    return answer

reward = [4,2,2,0,3,5]
health = [10,20,20,20,40,30]
optional = [1,0,1,0,0,0]


print(solution(reward, health, optional))