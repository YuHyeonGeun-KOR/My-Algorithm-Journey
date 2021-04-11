from collections import deque
import copy
def solution(rows, columns, queries):
    answer = []
    numpad = [[0]*columns for i in range(rows)]
    count = 1
    for i in range(rows):
        for j in range(columns):
            numpad[i][j] = count
            count +=1
    
    for test in queries:
        test_x1 = test[0]
        test_y1 = test[1]
        test_x2 = test[2]
        test_y2 = test[3]
        num_train = deque()
        y = test_y1-2
        x = test_x1-1 
        step = 1
        size_c = test_y2-test_y1+1
        size_r = test_x2-test_x1
        while True:
            for _ in range(size_c): 
                y+=step
                num_train.append(numpad[x][y])
                
            size_c -= 1
            if size_c < 1 and size_r  < 1:  
                break
            for _ in range(size_r): 
                x+=step
                num_train.append(numpad[x][y]) 
            size_r -= 1
            step = -step  

        check = (test_x2-test_x1 -1) * (test_y2-test_y1 -1) 
        if check != 0:
            temp =num_train[-(1+check)]
            del num_train[-(1+check)]
            num_train.insert(0,temp)
            checker = copy.deepcopy(num_train)
            for _ in range(check):
                del checker[-1]
            answer.append(min(checker))
            print(checker)
        else:
            temp =num_train[-1]
            del num_train[-1]
            num_train.insert(0,temp)
            answer.append(min(num_train))
            print(num_train)
        new_train = list(num_train)

        y = test_y1-2
        x = test_x1-1 
        step = 1
        size_c = test_y2-test_y1+1
        size_r = test_x2-test_x1
        ind = 0
        while True:
            for _ in range(size_c): 
                y+=step
                numpad[x][y] = new_train[ind]
                ind+=1
            size_c -= 1
            if size_c < 1 and size_r  < 1:  
                break
            for _ in range(size_r):  
                x+=step
                numpad[x][y] =  new_train[ind]
                ind+=1
            size_r -= 1
            step = -step  
    return(answer)
queries =[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
[[2,2,5,4],[3,3,6,6],[5,1,6,3]]
[[1,1,100,97]]

6 6 3 3 100 97

8 10 25
1 1 5 3
1
print(solution(3,3,queries))