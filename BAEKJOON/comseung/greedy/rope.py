import sys

input = sys.stdin.readline

n = int(input())

rope_list = []
max_w = 0

for i in range(n):
    w_input = int(input())
    rope_list.append(w_input)

rope_list.sort()

for i in range(len(rope_list)):
    max_w = max(max_w, rope_list[i] * (len(rope_list) - i ))

print(max_w)