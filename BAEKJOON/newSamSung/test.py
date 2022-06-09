from collections import deque

def cal (x , y , k,image):
    result = 0 
    row = len(image)
    cal = len(image[0])
    checker =[]
    for i in range(x-k//2 ,x-k//2+k ):
        for j in range(y-k//2 ,y-k//2+k):
            if i < 0 or i >=row  or j < 0 or j >= cal:
                continue
            else:
                result += image[i][j]
    return result // (k*k)

def solution(image, K):
    answer = [[] for _ in range(len(image)) ]
    index = 0
    for i in range(len(image)):
        for j in range(len(image[i])):
            answer[index].append(cal(i,j,K,image))
        index +=1
    

    

    return answer

image = [[4, 5, 2, 6, 7],
         [5, 4, 2, 4, 6],
         [6, 8, 4, 8, 7],
         [7, 3, 6, 6, 4],
         [5, 0, 4, 1, 5]]
    
print(solution(image,3))