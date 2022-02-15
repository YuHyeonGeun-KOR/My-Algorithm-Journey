from itertools import combinations

def prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
                    
                    
def solution(nums):
    answer = 0
    nums_com = list(combinations(nums,3))

    test= []
    for n in nums_com:
        if prime(sum(n)):
            test.append(sum(n))
            answer +=1
    return answer