input_current = input()
row = int(input_current[1])
column = int(ord(input_current[0])-int(ord('a')) ) + 1

moves = [
          (2,-1),(2,1),(-2,1),(-2,-1),
          (-1,-2),(-1,2),(1,2),(1,-2)
        ]

count = 0

for move in moves:
    next_row = row + move[0]
    next_column = column + move[1]

    if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <= 8 :
        count += 1

print(count)