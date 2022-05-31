import sys
input = sys.stdin.readline

n = int(input())
classRoom = list(map(int, input().split()))

coachMain , coachSub = map(int, input().split())

result = len(classRoom)

for Student in classRoom:
    Student -= coachMain
    
    if Student > 0:
        result += Student // coachSub
        if Student % coachSub > 0 :
            result +=1

print(result)

    