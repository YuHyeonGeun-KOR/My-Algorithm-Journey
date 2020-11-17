import sys
a =int(sys.stdin.readline())

b = [] 

for i in range(a):
    b.append(int(sys.stdin.readline()))

b.sort()

for j in range(len(b)):
    print(b[j])