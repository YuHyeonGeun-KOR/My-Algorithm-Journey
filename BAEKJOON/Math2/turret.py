n = int(input())

result = []
for i in range(n):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())

    
    d = ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))**0.5

    if d == 0 and r1==r2:
        result.append(-1)
        continue
    if  abs(r1-r2) < d <r1+r2:
        result.append(2)

    elif r1 + r2 == d or abs(r1-r2) == d:
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i)
