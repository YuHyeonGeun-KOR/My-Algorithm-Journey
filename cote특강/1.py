def is_perpect(num):
    if num <= 1:
        return False
    sum = 1
    for n in range(2,num):
        if num % n == 0:
            sum +=n
    return sum == num 

def perpect(nums):
    result = []
    for num in nums:
        if is_perpect(num):
            result.append(num)
    return result

print(perpect([1,5,3,6,8,34]))



