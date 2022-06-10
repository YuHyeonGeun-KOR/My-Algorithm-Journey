from curses.ascii import isdigit


def check(opstring  ,count , target , nlist ,idx , result,closFlag):
    print(opstring)
    rnum = 0 
    if opstring == '()':
        return
    if opstring != "" :
        try :
            rnum = eval(opstring)
        except:
            rnum = rnum
        
    if rnum > target:
            return
    if rnum == target :
        result.append(count)       

    if idx != len(nlist):
        if  isdigit(opstring[-1]):
            check(opstring + '+' , count  , target , nlist , idx , result , closFlag)
            check(opstring + '*' , count  , target , nlist , idx , result , closFlag)
            if closFlag == False :
                check(opstring + ')' , count  , target , nlist , idx  , result, True)
        else:
            if opstring[-1] == ')':
                check(opstring + '+' , count  , target , nlist , idx , result , closFlag)
                check(opstring + '*' , count  , target , nlist , idx , result , closFlag)
            check(opstring + str(nlist[idx]) ,count + 1, target , nlist , idx +1  , result, closFlag)

    return  result

def solution(numbers, target):
    answer = 0
    numbers = sorted(numbers)
    if numbers[0] == target:
        return 1
    if numbers[0] > target:
        return -1
    result = []
    answer = check("(" , 0, target , numbers , 0 , result , False)

    

    if len(answer) == 0 :
        return -1
    else:
        return min(answer)

print(solution([1,4,2] , 12))