input = [1,2,3,4,5,2,3,5]

left = 0
right = len(input) -1

for idx in range(len(input)):
    l_sum , r_sum = 0 ,0
    l_sum = sum(input[:idx])
    r_sum = sum(input[idx+1 :])

    if l_sum == r_sum :
        print([idx, input[idx] ,l_sum])
        
