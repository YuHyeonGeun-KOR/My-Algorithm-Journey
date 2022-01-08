from functools import update_wrapper
import sys
import operator
input = sys.stdin.readline

result = []
def night(user_point,guilty_point,mafia):
    mafia_point = user_point[mafia]
    for key, value in user_point.items():
        if key == mafia:
            continue
        elif user_point[key] < user_point[mafia]:
            


def day(user_point,guilty_point,night_count):
    die_num = max(user_point.iteritems(), key=operator.itemgetter(1))[0]
    del user_point[die_num]
    for key, value in user_point.items():
        user_point[key] = value + guilty_point[die_num][key]

    if len(user_point) == 1:
        result.append(night_count)
        return 
    else:
        night()

    
    

def play(user_point , guilty_point):
    if len(user_point)//2 == 0:
        #밤
    else:
       day()

    




p = int(input())

user = list(map(int, input().split()))
user_point = {}

idx = 0
for u in user:
    user_point[idx] = u
    idx +=1

guilty_point = []

for i in range(p):
    guilty_point.append(list(map, input().split()))

mafia_num = int(input())


