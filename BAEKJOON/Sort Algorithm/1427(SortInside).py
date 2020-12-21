##input number
num_list = list(map(int, input()))

##sorting Number
num_list.sort(reverse=True)

##print
for i in num_list:
    print(i, end='')