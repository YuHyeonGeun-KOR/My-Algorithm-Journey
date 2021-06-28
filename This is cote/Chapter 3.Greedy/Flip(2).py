import sys
input = sys.stdin.readline().rstrip

s = list(input().rstrip())
checker = int(s[0])
counter = [0 , 0]
for i in s:
    if i != checker:
        counter[int(checker)] +=1 
        checker = i
counter[int(checker)] +=1 
print(min(counter))