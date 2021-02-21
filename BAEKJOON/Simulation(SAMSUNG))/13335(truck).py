n, w, l = map(int, input().split())
right_side = list(map(int, input().split()))
bridge = []
left_side = []
time = 0
 
while len(left_side) != n:
 
    brdg = bridge[:]
 
    while brdg:
        b = brdg.pop(0)
        if time - b[1] == w:
            tr = bridge.pop(0)
            left_side.append(tr)
 
    if right_side:
        if sum(b[0] for b in bridge)+right_side[0] <= l:
            truck = right_side.pop(0)
            bridge.append((truck, time))
 
    time += 1
 
print(time)
