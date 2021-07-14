import sys
input = sys.stdin.readline

n,c = map(int, input().split())

house = []

for i in range(n):
    house.append(int(input()))

house= sorted(house)

start = house[0]
end = house[-1] - house[0]

result = 0
def b_search(array,target, start, end,result):
     
    while start <= end:
        mid = (start + end) //2
        count = 1 
        for i in range(1,len(array)):
            if array[i] >= start + mid:
                count += 1
                start = array[i]

        if count < target :
            end = mid -1
        else:
            start = mid +1
            result = mid
    return result
print(b_search(house,c,start,end,result))
