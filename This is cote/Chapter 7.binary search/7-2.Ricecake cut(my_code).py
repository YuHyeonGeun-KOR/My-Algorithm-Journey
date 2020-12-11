# 파라메트릭 서치
#최적화 문제를 결정문제로 바꾸어 해결
#원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제
#탐색범위 1~10억 -> 이진탐색트리
#이진탐색 최대 31번 , N이 최대 100만 -> 최대 3000만번의 연산

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid]  < target:
            start = mid +1
        else:
            end = mid - 1
    return end

N, m = map(int , input().split())

RiceCake =  list(map(int, input().split()))

RiceCake = sorted(RiceCake,reverse = True)
check_sum = 0
cut_sum = []
knife = RiceCake[0]

for i in  range(knife+1,1,-1):
    for j in RiceCake:
        if j-knife <= 0:
            check_sum += 0
        else:
            check_sum += (j-knife)

    cut_sum.append(int(check_sum))
    print(cut_sum)
    check_sum = 0
    knife -= 1

print(RiceCake[0]-binary_search(cut_sum,m,0,RiceCake[0]))