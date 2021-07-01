import sys
input = sys.stdin.readline
from itertools import combinations


INF = 1e9
N,M = map(int, input().split())

board = []

for i in range(N):
    board.append(list(map(int, input().split())))

chicken = []
house = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken.append((i,j))
        elif board[i][j] ==1:
            house.append((i,j))

chicken_distance = []


def dis_cal (a,b,c,d):
    return abs(a-b) + abs(c-d)
distance= 0
if M == len(chicken):
    for position_H in house:
        house_X , house_Y = position_H[0], position_H[1]
        distance_temp = INF
        for position_C in chicken:
            chicken_X , chicken_Y = position_C[0], position_C[1]
            distance_temp = min(distance_temp, dis_cal(chicken_X,house_X,chicken_Y,house_Y))
        distance += distance_temp
    chicken_distance.append(distance)
else:
    for new_chicken in combinations(chicken,M):
        distance= 0
        for position_H in house:
            house_X , house_Y = position_H[0], position_H[1]
            distance_temp = INF
            for position_C in new_chicken:
                chicken_X , chicken_Y = position_C[0], position_C[1]
                distance_temp = min(distance_temp, dis_cal(chicken_X,house_X,chicken_Y,house_Y))
            distance += distance_temp
        chicken_distance.append(distance)

print(min(chicken_distance))