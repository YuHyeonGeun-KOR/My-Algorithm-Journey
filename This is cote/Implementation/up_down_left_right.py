X = 1
Y = 1

N = int(input())
direct_lists = list(input().split())

for direct_list in direct_lists:
    if direct_list == "R" and Y < N:
        Y += 1
    elif direct_list == "L"and Y > 1:
        Y -= 1     
    elif direct_list == "D"and X < N:
        X += 1     
    elif direct_list == "U"and X > 1:
        X -= 1     
    else :
        continue

print(X,Y)