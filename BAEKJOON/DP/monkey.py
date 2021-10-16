import sys
input = sys.stdin.readline

max_level = int(input())

char_count = list(map(int, input().split()))

power = list(map(int, input().split()))

day = int(input())
visited = {}
for i in range(day+2):
    visited[i] = []
result = -1e9
def cal_power(d, char):
    global result 
    global visited
    
    if d > day:
        n_power = 0 
        
        for i in range(len(char)):
            n_power+= (char[i] * power[i])
        
        result = max(result, n_power)
        return

    for i in range(len(char)):
        cal_power(d+1 , char)
        if char[i] >0 and i < len(char)-1:
            char[i]-=1
            char[i+1]+=1
            cal_power(d+1 , char)
            char[i]+=1
            char[i+1]-=1
            

cal_power(0 ,char_count)
print(result)
    
