import sys
input = sys.stdin.readline

n = int(input())


board = []
num = [
    [[1], [1, 4], []],
    [[1, 2, 3, 7], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 6]],
    [[1, 7], [0, 1, 7], []],
    [[1, 3, 4, 5, 7, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [2]],
    [[1, 4, 7], [1, 4, 7], []]]

for _ in range(5):
    board.append(list(input().rstrip()))

number = []


for i in range(0, len(board[0]), 4):
    checker = [False for i in range(10)]
    if i % 4 == 3:
        continue

    for j in range(5):
        for k in range(3):
            if board[j][i+k] == '#':
                for l in num[j][k]:
                    checker[l] = True

    candidate = []
    for m in range(10):
        if checker[m] == False:
            candidate.append(m)

    number.append(candidate)

count = 1

for i in number:
    count *= len(i)
    
if count == 0 :
    print(-1)
else:
    result = 0

    for key, i in enumerate(number):
        result += sum(i) * (10 ** (len(number) - key - 1)) * (count / len(i))

    print(round(result / count, 5))
