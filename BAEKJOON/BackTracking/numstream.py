import sys 
input = sys.stdin.readline

n = int(input())
def recur (now):
    for part_len in range(1, len(now)//2+1):
        for part_start in range(part_len, len(now) - part_len + 1):
            if now[part_start - part_len:part_start] == now[part_start:part_start + part_len]:
                return False			# False 리턴
    return True

def dfs (answer , length):
    if len(answer) == length:
        print(answer)
        exit()

    for i in "123":
        if recur(answer + i) == True:
            answer = answer + i
            dfs(answer , length)
    return    
answer = "1"
dfs(answer , n)
    