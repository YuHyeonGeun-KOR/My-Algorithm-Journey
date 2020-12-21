n = int(input())

number = []
ze = [1,0,1] 
one = [0,1,1]

for i in range(n):
    number.append(int(input()))

   
def fibonacci(x) :
    if len(ze) <=x :
        for i in range (len(ze),x+1):
            ze.append(ze[i-1]+ze[i-2])
            one.append(one[i-1]+one[i-2])

    print(ze[x],one[x])   
    


for i in number:
    fibonacci(i)

