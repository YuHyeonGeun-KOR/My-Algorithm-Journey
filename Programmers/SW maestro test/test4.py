import itertools 
def main():
    x = input().split()
    n = int(input())
    skill = []
    for i in range(n):
        skill.append(list(map(str,input().split())))
    hit = x[0]
    print(skill)
    result = []
    for i in range(len(skill)):
        if skill[i][0] == hit:
            result.append(i)
            del skill[i]
    
    for i in skill:
        if i[0] == hit:
            result.append(i)
    print(skill)
    print(result)
if __name__=="__main__":
    main()