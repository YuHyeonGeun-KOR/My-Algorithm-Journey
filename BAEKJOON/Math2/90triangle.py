import sys
input = sys.stdin.readline

while True:
    side = list(map(int, input().split()))
    if  side[0]==0 and side[1] == 0 and side[2] == 0:
        break

    side = sorted(side)

    if (side[0] * side[0]) + (side[1] * side[1]) == side[2]*side[2]:
        print("right") 
    else:
        print("wrong")   