

result = []
while True:
    l,p,v  = map(int, input().split())

    if l == 0 and p == 0 and v == 0:
        break
    
    result.append( l * (v//p) + min((v%p) , l))


for i in range(len(result)):
    print("Case " + str(i+1) + ": " + str(result[i]) )
