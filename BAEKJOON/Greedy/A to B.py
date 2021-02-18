a,b = map(int, input().split())
result = 0
while True:
    if b == a:
        print(result+1)
        break
    elif b < a:
        print(-1)
        break

    if b % 2 == 0:
        b= b//2
        result += 1
    elif b % 10 == 1:
        b = b//10
        result += 1   
    else:
        print(-1)
        break 