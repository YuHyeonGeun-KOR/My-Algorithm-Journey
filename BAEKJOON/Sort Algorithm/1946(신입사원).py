import sys 
input = sys.stdin.readline
n = int(input())
result = []
for i in range(n):
    t = int(input())
    new = 1
    candidate = [0]*(t+1)
    for j in range(t):
        test1,test2 = map(int,input().split())
        candidate[test1] = test2
    test2_score = candidate[1]
    for k in range(2,t+1):
        if candidate[k] < test2_score:
            test2_score = candidate[k]
            new+=1
        else:
            continue
    result.append(new)
for i in range(n):
    print(result[i])
