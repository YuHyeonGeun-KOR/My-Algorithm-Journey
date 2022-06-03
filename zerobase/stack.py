import sys
input = sys.stdin.readline

n = int(input())

stack = []
answer = []

start = 1
for i in range(n):
    num = int(input())
    stackFlag = False
    for j in range(start , num+1):
        stack.append(j)
        answer.append("+")
        start = j
        stackFlag = True

    if stackFlag == True:
        start +=1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        exit(0)

for op in answer:
    print(op)






