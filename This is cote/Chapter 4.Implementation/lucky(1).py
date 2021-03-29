import sys
input= sys.stdin.readline
score = list(input())

l = len(score)

mid = l//2
left = 0
right = 0
for i in range(mid):
    left += int(score[i])
    right += int(score[mid+i])



if left == right :
    print("LUCKY")
else:
    print("READY")