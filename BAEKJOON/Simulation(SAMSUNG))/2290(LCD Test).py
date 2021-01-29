import sys
input = sys.stdin.readline

s, n = map(int, input().split())

n_list = []
for i in str(n):
    n_list.append(i)


result = [[] for i in range(0,2*s+3)]


def one(s,result):
    for i in range(0,2*s+3):
        if i % (s + 1) == 0 :
            result[i].append(" "*(s+2))
            result[i].append(" ")
        elif  i < s + 1:
            result[i].append(" "*(s+1))
            result[i].append("|")
            result[i].append(" ")
        else:
            result[i].append(" "*(s+1))
            result[i].append("|")
            result[i].append(" ")
    return result

def two(s,result):
    for i in range(0,2*s+3):
        if i % (s + 1) == 0 :
            result[i].append(" ")
            result[i].append("-" * s)
            result[i].append(" ")
            result[i].append(" ")
        elif  i < s + 1:
            result[i].append(" " * (s+1))
            result[i].append("|")
            result[i].append(" ")
        else:
            result[i].append("|")
            result[i].append(" " * (s+1))
            result[i].append(" ")            
    return result

def three (s,result):
    for i in range(0,2*s+3):
        if i % (s + 1) == 0 :
            result[i].append(" ")
            result[i].append("-" * s)
            result[i].append(" ")
            result[i].append(" ")
        else:
            result[i].append(" " * (s+1))
            result[i].append("|")
            result[i].append(" ")
    return result

def four (s,result):
    for i in range(0,2*s+3):
        if i  == 0 :
            result[i].append(" " *(s+2))
            result[i].append(" ")
        elif  i < s + 1:
            result[i].append("|")
            result[i].append(" " * (s))
            result[i].append("|")
            result[i].append(" ")
        elif i  == (s+1):
            result[i].append(" ")
            result[i].append("-"*s)
            result[i].append(" ")
            result[i].append(" ")
        elif  i > s + 1 and i % (s + 1) != 0:
            result[i].append(" " * (s+1))
            result[i].append("|")
            result[i].append(" ")
        else:
            result[i].append(" " * (s+2))
            result[i].append(" ")
        
    return result


def five(s,result):
    for i in range(0,2*s+3):
        if i % (s + 1) == 0 :
            result[i].append(" ")
            result[i].append("-" * s)
            result[i].append(" ")
            result[i].append(" ")
        elif  i > s + 1:
            result[i].append(" " * (s+1))
            result[i].append("|")
            result[i].append(" ")
        else:
            result[i].append("|")
            result[i].append(" " * (s+1))
            result[i].append(" ")            
    return result

def six(s,result):
    for i in range(0,2*s+3):
        if i % (s + 1) == 0 :
            result[i].append(" ")
            result[i].append("-" * s)
            result[i].append(" ")
            result[i].append(" ")
        elif  i > s + 1:
            result[i].append("|")
            result[i].append(" " * (s))
            result[i].append("|")
            result[i].append(" ")
        else:
            result[i].append("|")
            result[i].append(" " * (s+1))
            result[i].append(" ")            
    return result

def seven(s,result):
    for i in range(0,2*s+3):
        if i == 0 :
            result[i].append(" ")
            result[i].append("-" * s)
            result[i].append(" ")
            result[i].append(" ")
        elif  i % (s + 1) == 0 :
            result[i].append(" " * (s+2))
            result[i].append(" ")
        else:
            result[i].append(" " * (s+1))
            result[i].append("|")
            result[i].append(" ")            
    return result

def eight(s,result):
    for i in range(0,2*s+3):
        if i % (s + 1) == 0 :
            result[i].append(" ")
            result[i].append("-" * s)
            result[i].append(" ")
            result[i].append(" ")
        else:
            result[i].append("|")
            result[i].append(" " * (s))
            result[i].append("|")
            result[i].append(" ")          
    return result

def nine(s,result):
    for i in range(0,2*s+3):
        if i % (s + 1) == 0 :
            result[i].append(" ")
            result[i].append("-" * s)
            result[i].append(" ")
            result[i].append(" ")
        elif  i < s + 1:
            result[i].append("|")
            result[i].append(" " * (s))
            result[i].append("|")
            result[i].append(" ")
        elif  i > s + 1:
            result[i].append(" " * (s+1))
            result[i].append("|")
            result[i].append(" ")        
        else:
            result[i].append("|")
            result[i].append(" " * (s))
            result[i].append("|")
            result[i].append(" ")          
    return result

def zero(s,result):
    for i in range(0,2*s+3):
        if i == 0 or i == 2*(s+1):
            result[i].append(" ")
            result[i].append("-" * s)
            result[i].append(" ")
            result[i].append(" ")
        elif  i < s + 1 or i > s + 1:
            result[i].append("|")
            result[i].append(" " * (s))
            result[i].append("|")
            result[i].append(" ")
        elif  i > s + 1:
            result[i].append(" " * (s+1))
            result[i].append("|")
            result[i].append(" ")        
        else:
            result[i].append(" " * (s+2))
            result[i].append(" ")          
    return result

for i in range(0,len(n_list)):
    if n_list[i] == '1':
        one(s,result)
    elif n_list[i] == '2':
        two(s,result)
    elif n_list[i] == '3':
        three(s,result)
    elif n_list[i] == '4':
        four(s,result)    
    elif n_list[i] == '5':
        five(s,result)  
    elif n_list[i] == '6':
        six(s,result)      
    elif n_list[i] == '7':
        seven(s,result)     
    elif n_list[i] == '8':
        eight(s,result)  
    elif n_list[i] == '9':
        nine(s,result) 
    elif n_list[i] == '0':
        zero(s,result)        

for i in range(2*s+3):
        r  = "".join(result[i])
        print(r)