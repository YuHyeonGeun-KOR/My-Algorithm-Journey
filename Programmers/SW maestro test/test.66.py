def bst(array,result , start , end):
    while start <= end :
        mid = (start + end) // 2
        left = array[start:mid]
        right = array[mid:end]
        if len(left) == 0 or len(right)==0:
            return result
        if max(left) > max(right):
            result += max(left)
            start = mid 
            bst(array,result , start , end)
        elif max(left) < max(right):
            result += max(right)
            end = mid - 1
            bst(array,result , start , end)
        
    return result

def main():
    x = int(input())
    work = list(map(int,input().split()))
    result = 0
    print(bst(work,result,0,x))
    
    
if __name__=="__main__":
    main()