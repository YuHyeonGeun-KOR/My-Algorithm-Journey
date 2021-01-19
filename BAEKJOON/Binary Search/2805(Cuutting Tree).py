import sys
input = sys.stdin.readline

n, m = map(int, input().split())

Tree =  list(map(int, input().split()))

e = max(Tree)


def bst (array, target , start , end):
    while start <=  end:
        mid = (start + end) // 2 
        total = 0
        for x in array :
            if (x - mid) >=0:
                total += (x-mid)
        
        if total < target:   
            end = mid - 1 
        elif total >=target:
            start = mid + 1 
            answer = mid
    return answer        

print(bst(Tree,m,0,e))
        
