n,l = map(int, input().split())

lick = list(map(int,input().split()))
lick = sorted(lick)
start = 0.5
count  = 0
for i in lick:
    if start < i:
        start = i - 0.5 + l 
        count +=1

    
print(count)

    

    