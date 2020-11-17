import sys
a =int(sys.stdin.readline())

b = [0]*10001


for i in range(0,a):
    c = int(sys.stdin.readline())
    b[c-1] = b[c-1] + 1


for j in range(10000):
   if b[j] != 0:
       for k in range(b[j]):
           print(j+1)