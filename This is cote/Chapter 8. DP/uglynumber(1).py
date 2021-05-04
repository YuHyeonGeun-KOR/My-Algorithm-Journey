n = int(input())

ugly_num = []

for i in range(1,1001):
    num_list = []
    checker = i
    while True:
        if checker % 2 == 0:
            checker = checker//2    
        elif checker % 3 == 0:
            checker = checker//3
        elif checker % 5 == 0:
            checker = checker//3
        elif checker == 1:
            ugly_num.append(i)
            break
        elif checker !=1:
            break
print(ugly_num[n-1])