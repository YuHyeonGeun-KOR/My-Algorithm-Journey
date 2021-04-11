import copy
def solution(key, lock):
    m = len(key[0])
    n = len(lock[0])
    y = []
    x = []
    answer = False
    def rotated(a):
        r_y = len(a)

        result = [[0]* r_y for _ in range(r_y)]

        for i in range(r_y):
            for j in range(r_y):
                result[j][r_y-i-1] = a[i][j]
        return result
    

    for i in range(n - m +1):
        for j in range(n -m +1):
            count =0
            
            for k in range(4):
                key = rotated(key)
                lock_copy = copy.deepcopy(lock)
                check_point = lock_copy[j:j+m][i:i+m]
                for l ,p in zip(key,check_point):
                    for o in range(len(key)):
                        p[o] = (l[o] + p[o])
                print(lock_copy)
                for l_check in lock_copy :
                    if 0 not in l_check and 2 not in l_check:
                        count +=1
                if count == len(lock):
                    return True        
                else:
                    count = 0    
    return answer


key = [[0, 1, 0], [0, 1, 0], [0, 0, 0]]
lock = [[1, 1, 1, 1], [1, 1, 1,1], [0,0, 1, 1],[1,1,1,1]]
print(solution(key,lock))