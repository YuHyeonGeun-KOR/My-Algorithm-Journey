import sys
import copy
input = sys.stdin.readline

W, H, f, c, x1, y1, x2, y2 = map(int, input().split())



last_square = (x2 - x1) * (y2 - y1) * (c+1)

result = 0 
if f <= W // 2:
    if f <= x1:
        result = W * H - last_square
    
    else :
        result = W * H - (last_square + (min(f, x2) - x1) * (y2 - y1) * (c+1))
    

else :
    if W <= x1 + f :
        result = W * H - last_square
    else :
        result =  W * H - (last_square + (min(W, f + x2) - (f + x1)) * (y2 - y1) * (c+1))
    
print(result)
