n = int(input())

transport = list(input())
checker = [0]*(n)

for i in range(0,n):
    if i+1 == n-1:
        if transport[i] =='0'or transport[i-1] == '0':
            if checker[i-2] == 0:
                checker[i+1] = 1    
            else:
                checker[i+1] = checker[i-2]
            break
        else:
            break
    elif transport[i] == '0':
        checker[i+1] = checker[i]
        checker[i+2] = checker[i]
        continue
    else:
        if (transport[i+1] == '0'):
            if checker[i+1] ==0: 
                checker[i+1] = checker[i]
        elif transport[i+2] == '0':
            if checker[i+2] ==0:
                checker[i+2] = checker[i]
        else:
            checker[i+1] = checker[i+1]+1
            checker[i+2] = checker[i]+2
        

print(checker[-1])
# 다시 풀어보기

    

