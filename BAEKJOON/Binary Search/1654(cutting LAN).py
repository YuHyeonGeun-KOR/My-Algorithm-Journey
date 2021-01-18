import sys
input = sys.stdin.readline

k, n = map(int, input().split())

LAN = []
for i in range(k):
    cm = int(input())
    LAN.append(cm)

s = 1
e = max(LAN)

def bst (array, target , start , end):
    while start <=  end:
        mid = (start + end) // 2 
        total = 0
        for x in array :
            total += (x // mid)
        
        if total < target:   
            end = mid - 1 
        elif total >=target:
            start = mid + 1 
            answer = mid
    return answer

print(bst(LAN,n,1,e))
        
