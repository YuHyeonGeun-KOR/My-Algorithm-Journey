from collections import deque
number_quque = deque(list(input()))

print(number_quque)

num_1 = int(number_quque.popleft())
num_2 = int(number_quque.popleft())
num_sum = 0
if num_1 == 0 or num_2 == 0:
    num_sum = num_1 + num_2
else :
    num_sum = num_1 * num_2


for i in range(len(number_quque)):
    num_1 = int(number_quque.popleft())
    if num_1 == 0 :
        continue
    else :
        num_sum = num_sum * num_1

print(num_sum)