import sys
input = sys.stdin.readline().rstrip

s = input()
s = list(s)

s_check = [0,0]
checker = s[0]
for i in s:
    if i == checker:
        continue
    else:
        s_check[int(checker)] +=1
        checker = i
s_check[int(checker)] +=1

print(min(s_check[0],s_check[1]))