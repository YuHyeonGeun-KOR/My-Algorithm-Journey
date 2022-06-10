import sys
input = sys.stdin.readline

n = int(input())
answer = []
for i in range(n):
    checker = list(input().rstrip())
    right = 0
    no_Flag = False
    while checker:
        now = checker.pop()
        if now == ")":
            right +=1
        else:
            if right >= 1:
                right -=1
            else:
                no_Flag = True

    if no_Flag == False and right == 0 :
        answer.append("YES")
    else:
        answer.append("NO")

for a in answer:
    print(a)
