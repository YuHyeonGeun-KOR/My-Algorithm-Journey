import sys
input = sys.stdin.readline


t = int(input())

for i in range(t):
    n = int(input())
    
    
    Tree_list = list(map(int,input().split()))
    Tree_list.sort()
    
    result = 0
    
    for j in range(2,n):
        difficulty = Tree_list[j] - Tree_list[j - 2]
        result = max(difficulty, result)
    
    print(result)