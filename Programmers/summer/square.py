def GCD(w,h):
    a = w
    b = h
    
    if w<h:
        a = h
        b = w
        
    while b > 0:
        a, b = b, a % b
    
    return a 

def solution(w,h):
    
    gcd_num = (GCD(w,h))
    if gcd_num ==1:
        return w*h - (w+h-1)
    else:
        return w*h - (w+h - gcd_num)
    

print(solution(8,12))