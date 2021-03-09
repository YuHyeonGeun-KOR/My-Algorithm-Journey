import sys
input = sys.stdin.readline

n, k = map(int, input().split())

Level = []
for i in range(n):
    l = int(input())
    Level.append(l)


answer = 0
start = min(Level)
end = max(Level)

def bst (array,k, start , end):
    while start <=  end:
        result =0
        
        mid = (start + end) // 2 
        
        for x in array :
            if x >= mid:
                continue
            else:
                result += (mid-x)
        
        if result <= k:  
            answer = mid
            start = mid + 1 
        elif result > k:
            end = mid - 1
    
    return answer
print(bst(Level,k,start,end))