num = 1
tri_list = [1] 
tri_num = 0
while tri_num <1000:
    
    tri_num = num*(num + 1) / 2
    tri_list.append(tri_num)
    num += 1

def Eureka (check_num):

    for i in range(len(tri_list)):
        for j in range(len(tri_list)):
            for k in range(len(tri_list)):
                if tri_list[i] + tri_list[j] + tri_list[k] == check_num:
                    return True
    
    return False


n= int(input())
result = []
for i in range(n):
    check_num = int(input())
    if Eureka(check_num):
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i)


