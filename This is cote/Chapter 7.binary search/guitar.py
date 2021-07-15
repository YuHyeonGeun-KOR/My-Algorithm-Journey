import sys

input = sys.stdin.readline

n,m = map(int, input().split())

lesson = list(map(int, input().split()))

start = max(lesson)
end = sum(lesson)

def b_search(array,target,start, end):
    result = 1e9
    while start<=end:
        lesson_time = 0
        count = 0
        mid = (start+end) // 2
        lesson_counter = 0
        for i in range(n):
            if lesson_time + array[i] > mid:
                count +=1
                lesson_time = 0
            else:
                lesson_counter +=1
            lesson_time += array[i]

        if lesson_counter != n:
            count +=1   


        if count <= target:
            end = mid  - 1
            result = min(result, mid)
        else:
            
            start = mid  + 1
    return result

print(b_search(lesson,m,start , end))