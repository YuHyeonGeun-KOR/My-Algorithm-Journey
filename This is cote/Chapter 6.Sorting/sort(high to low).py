N =int(input())

List = []
for i in range(N):
    List.append(int(input()))

array = sorted(List,reverse=True)

for i in array:
    print(i,end = " ") 