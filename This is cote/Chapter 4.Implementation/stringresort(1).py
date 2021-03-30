"""
import heapq

string = list(input())
h = []
num_sum = 0
for i in string:
    if 48 <= ord(i) <= 57:
        num_sum += int(i)
    elif 65 <= ord(i) <= 90:
        h.append(i)

heapq.heapify(h)

print(h)
print(num_sum) 
"""

string = list(input())
h = []
num_sum = 0
for i in string:
    if 48 <= ord(i) <= 57:
        num_sum += int(i)
    elif 65 <= ord(i) <= 90:
        h.append(i)

h.sort()
alpha = ''.join(h)
print(alpha + str(num_sum))


