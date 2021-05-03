import sys
input = sys.stdin.readline

n = int(input())
triangle = []
for i in range(n):
    triangle.append(list(map(int,input().split())))

sum_list =[[] for _ in range(n)]

sum_list[0].append(int(triangle[0][0]))
for i in range(1,n):
    
    for j in range(len(triangle[i])):
        if j == 0 :
            sum_list[i].append(int(triangle[i][0]) + int(sum_list[i-1][j]))
        elif j == len(triangle[i])-1:
            sum_list[i].append(int(triangle[i][j]) + int(sum_list[i-1][j-1]))
        else:
            sum_list[i].append(max( (sum_list[i-1][j-1] +  triangle[i][j]) , (sum_list[i-1][j] + triangle[i][j])))
    
print(max(sum_list[n-1]))
