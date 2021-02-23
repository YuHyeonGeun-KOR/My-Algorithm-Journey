import copy
n, w, l = map(int, input().split())
wait = list(map(int, input().split()))
bridge = []
crossed = []
sum_num =0
time = 0
 
while len(crossed) != n:
 
    bridge_copy = copy.deepcopy(bridge)
    
    while len(bridge_copy) != 0:
        checker = bridge_copy[0]
        del bridge_copy[0]
        if time - checker[1] == w:
            crossed.append(bridge[0])
            del bridge[0]

    if wait:
        sum_num =0
        for i in bridge:
            sum_num += i[0]
        checker = sum_num + wait[0]
        if checker <= l:
            bridge.append((wait[0], time))
            del wait[0]
            
    time += 1
 
print(time)
