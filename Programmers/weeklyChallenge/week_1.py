def solution(price, money, count):
    answer = -1

    total_sum  =  ( (count) * (count +1) // 2 ) * price
    
    if  total_sum > money :
        return total_sum - money
    else:
        return 0