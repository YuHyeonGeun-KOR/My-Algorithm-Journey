X = 1
Y = 1

N = int(input())
direct_list = list(input().split())

for i in range(len(direct_list)):
    if direct_list[i] == "R" and Y < N:
        Y += 1
    elif direct_list[i] == "L"and Y > 1:
        Y -= 1     
    elif direct_list[i] == "D"and X < N:
        X += 1     
    elif direct_list[i] == "U"and X > 1:
        X -= 1     
 
print(X,Y)