N,M = map(int,input().split())

current_X,current_Y,D =  map(int,input().split())

Filed = [[int(x) for x in input().split()] for _ in range(N)]

check = [[0]*M for j in range(N)]
result = 0
count = 0

Left = [(0,-1),(1,0),(0,1),(-1,0)] 
Back = [(-1,0),(0,-1),(1,0),(0,1)]

check[current_Y][current_X] = 1

print(check)
print(current_Y+Left[D][0])
print(current_X + Left[D][1])

while(1) :
    if Filed[current_Y+Left[D][0]][current_X + Left[D][1]] == 0 and check[current_Y+Left[D][0]][current_X + Left[D][1]] == 0:
        D -= 1
        if D < 0 :
            D = 3
            count = 0 
    
        current_Y = current_Y+Left[D][0]
        current_X = current_X+Left[D][1]

        result += 1

    elif Filed[current_Y+Left[D][0]][current_X + Left[D][1]] == 1 or check[current_Y+Left[D][0]][current_X + Left[D][1]] == 1 :
        D -= 1
        if D < 0 :
            D = 3
        count += 1


    if count == 4 :
        count = 0
        current_Y = current_Y+Back[D][0]
        current_X = current_X+Back[D][1]
        if Filed[current_Y][current_X] == 1 :
            break


print(result)        