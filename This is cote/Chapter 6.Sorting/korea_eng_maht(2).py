import sys
input = sys.stdin.readline

n = int(input())


list = []
for i in range(n):
    list.append(input().split())

result = sorted(list,key = lambda x  : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in result :
    print(i[0])