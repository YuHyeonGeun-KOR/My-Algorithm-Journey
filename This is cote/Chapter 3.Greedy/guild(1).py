import sys
input = sys.stdin.readline

n = int(input())

member = list(map(int, input().split()))
member_num = {}

result =0

for i in member:
    if i not in member_num:
        member_num[i] = 1
    else:
        member_num[i] +=1

for m,m_n in member_num.items():
    if m_n >= m:
        result += 1

print(result)






