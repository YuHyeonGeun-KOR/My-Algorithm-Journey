n = int(input())


num_list = list(map(int,input().split()))
num_list.reverse()
new_list = [0] *(2*n)
new_list[0] = num_list[0]


def bst(start, end , array,target):
    while start< end:
        mid = (start+end) //2
        if array[mid] > target:
            start = mid+ 1
        elif array[mid] < target:

for i in range(n):
    for j in range(i):
        if num_list[j] > new_list[i] :
            new_list[i+1] = num_list[j]
        else:
            
...
        
print(count)  
    