import sys 
input = sys.stdin.readline

n = int(input())

tree = []
result = []
for i in range(n):
    tree.append(list(map(int, input().split())))
    result.append([0] * (i+1))


result[0][0] = tree[0][0]

dy = [-1,0]
for i in range(1,n):
    for j in range(len(result[i])):
        
        for idx in range(2):
            ny = j + dy[idx] 

            if ny <=-1 or ny >=len(result[i-1]):
                continue

            result[i][j] = max(result[i][j] , (tree[i][j] + result[i-1][ny]))


print(max(result[-1]))
