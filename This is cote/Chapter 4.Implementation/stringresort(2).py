import sys
input = sys.stdin.readline

s = list(input().rstrip())


s.sort()

result  = ""
sum_val = 0
for i in s:
    if i.isdigit():
        sum_val += int(i)
    else:
        result +=i

print(result + str(sum_val))
