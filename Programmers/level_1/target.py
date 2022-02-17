def calcul(numbers, index , sumNum , target):
    global answer
    if index >= len(numbers):
        if sumNum == target:
            answer +=1
            return True
        return False
    sumNum += numbers[index]
    calcul(numbers, index+1 , sumNum , target)
    sumNum -= numbers[index]
    sumNum += -numbers[index]
    calcul(numbers, index+1 , sumNum , target)
    return 

answer = 0

def solution(numbers, target):
    index = 0 
    calcul(numbers, index , 0, target)
    
    return answer