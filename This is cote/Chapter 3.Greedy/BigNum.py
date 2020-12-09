# intput N,M,K 
N,M,K = map(int, input().split())
# input List of number
num_list = list(map(int, input().split()))

#Sorting list and reverse
num_list.sort()
num_list.reverse()

#Initialize Var
count = 0
result = 0

#Calculating
for i in range(0,M): 
    if count < K:
        result += num_list[0]
        count += 1
    elif count == K:
        result +=  num_list[1]
        count = 0

#print result 
print(result)