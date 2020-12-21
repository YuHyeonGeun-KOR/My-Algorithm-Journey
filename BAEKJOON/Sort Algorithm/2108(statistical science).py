import sys  ## input , output
import statistics ## find middle Value

num_arr = int(sys.stdin.readline())

arr  = []
count = [0]*8001

sum_all = 0
max_num = 0
min_num = 0
Freq = 0
Freq_num = 0

##set values
for i in range(0,num_arr):
    num_check = int(sys.stdin.readline())
    arr.append(num_check)
    
    if num_check < 0 :
        count[(num_check*-1)+4000] += 1    
    else :
        count[num_check] += 1
    
    sum_all = sum_all + arr[i]
    
    if i == 0:
        max_num = arr[0]
        min_num = arr[0]
    else :
        if arr[i]>max_num:
            max_num = arr[i]
        elif arr[i]<min_num:
            min_num = arr[i]


##Find Frequent Value
Freq = max(count)
Freq_arr = []
for i in range(0,8001):
    v = count[i]

    if v == Freq and i <=4000:
        Freq_arr.append(i)
    elif v == Freq and i >4000:   
        Freq_arr.append((i*-1)+4000)
    
## Find Frequency number
Freq_arr.sort()
len_Feq = len(Freq_arr)
if len_Feq == 1:
    Freq_num = Freq_arr[0]
else:
    Freq_num = Freq_arr[1]                



##Sorting array and Finding middle of array 
arr.sort()
mid_value =statistics.median(arr)



##print result
print(round(sum_all/num_arr))
print(mid_value)
print(Freq_num)
print(max_num-min_num)





