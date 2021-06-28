import sys
input = sys.stdin.readline

dx = [2,2,-2,-2,1,-1,1,-1]
dy = [1,-1,-1,1,2,2,-2,-2]

p = input()

col = p[0]
row = p[1]
print(col)
count = 0 
for i in range(8):
    if ord('a') <= ord(col) + dx[i] <= ord('h') and 1 <= int(row) + dy[i] <= 8:
        count +=1 

print(count)


