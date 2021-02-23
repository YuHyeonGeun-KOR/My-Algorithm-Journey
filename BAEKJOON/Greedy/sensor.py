n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
distance = []
result = 0
if k < n: 
    sensor.sort()
    for i in range(1, n):
        distance.append(sensor[i] - sensor[i-1])
    distance.sort(reverse=True)

    for i in range(k-1):
        del distance[0]
    
    result = sum(distance)
    print(result)
else:
    print(result)