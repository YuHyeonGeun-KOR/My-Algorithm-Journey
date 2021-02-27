def solution(brown, yellow):
    answer = []
    b = (4-brown)
    D = (b**2) - (4*2*2*yellow)
    x1 =0
    x2 =0
    x = 0 
    if D>0:
        x1 = (-b + D**0.5) / (2*2)
        x2 = (-b - D**0.5) / (2*2)
    elif D==0:
        x = -b / 2*2
    

    row = 0
    col = 0
    if x1 >= 0 and D >0:
        row = x1
    elif x2 >= 0 and D >0 :
        row = x2
    else:
        row = x

    col = yellow // row
    answer = [row+2,col+2]
    print(answer)
    return answer

brown = 8
yellow = 1 

solution(brown,yellow)