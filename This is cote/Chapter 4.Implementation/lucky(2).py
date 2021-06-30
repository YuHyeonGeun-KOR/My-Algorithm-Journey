import sys
input = sys.stdin.readline

s = input().rstrip()

start  = 0
end = len(s)-1
left = 0
right = 0

while(start<end):
    left += int(s[start])
    right += int(s[end])
    
    start +=1
    end -=1

if left == right :
    print("LUCKY")
else:
    print("READY")

