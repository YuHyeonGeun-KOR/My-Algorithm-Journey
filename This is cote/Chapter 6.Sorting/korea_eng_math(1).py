import sys
input = sys.stdin.readline
n = int(input())
score = [[] for _ in range(n)]
for i in range(n):
    name, kor, eng, math = input().split()
    score[i].append(name)
    score[i].append([int(kor),int(eng),int(math)])

score_sorted = sorted(score,key = lambda x : (-x[1][0] , x[1][1], -x[1][2] , x[0]))

for i in range(n):
    print(score_sorted[i][0])