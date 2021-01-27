import sys 
input = sys.stdin.readline


declare = list(input().split())
order = []
declare[-1] = declare[-1].replace(";","")

for i in range(1, len(declare)):
    result = declare[0]
    name = ""
    declare[i] = declare[i].replace(",","",1)

    j=0
    
    while  j <len(declare[i]):
        if declare[i][j] !="&" and declare[i][j] !="*" and declare[i][j] !="[" and declare[i][j] !="]" :
            name +=  declare[i][j]
        j+=1    
        
    

    for k in range(len(declare[i])-1,-1,-1):
        if declare[i][k] == "&":
            result += "&"
        elif declare[i][k] == "*":
            result += "*"
        elif declare[i][k] == "]":
            result += "[]"
        else :
            continue
            
    
    
    result += (" ")
    result += (name)
    result += (";")
    order.append(result)

for i in range(0,len(order)):
    print(order[i])
