def solution(holidays, k):
    answer = -1
    one = [0]*31
    two = [0]*28
    three = [0]*31
    four = [0]*30
    five = [0]*31
    six = [0]*30
    seven = [0]*31
    eight = [0]*31
    nine = [0]*30
    ten = [0]*31
    eleven = [0]*30
    twelve = [0]*31
    result = []
    checker = 0
    for i in range(1,len(one)+1):
        if (i - 2) % 7 == 0 or (i - 3) % 7 == 0 :
            one[i-1] = 1 
   
    for i in range(1,len(two)+1):
        if (i + 1) % 7 == 0 or i % 7 == 0 :
            two[i-1] = 1 

    for i in range(1,len(three)+1):
        if (i + 1) % 7 == 0 or i % 7 == 0 :
            three[i-1] = 1 

    for i in range(1,len(four)+1):
        if (i - 3) % 7 == 0 or (i - 1) % 7 == 0 :
            four[i-1] = 1 

    for i in range(1,len(five)+1):
        if (i - 1) % 7 == 0 or (i - 2) % 7 == 0 :
            five[i-1] = 1 

    for i in range(1,len(six)+1):
        if (i - 5) % 7 == 0 or (i - 6) % 7 == 0 :
            six[i-1] = 1 

    for i in range(1,len(seven)+1):
        if (i - 3) % 7 == 0 or (i - 4) % 7 == 0 :
            seven[i-1] = 1 

    for i in range(1,len(eight)+1):
        if i % 7 == 0 or (i - 1) % 7 == 0 :
            eight[i-1] = 1 

    for i in range(1,len(nine)+1):
        if (i - 4) % 7 == 0 or (i - 5) % 7 == 0 :
            nine[i-1] = 1 

    for i in range(1,len(ten)+1):
        if (i - 2) % 7 == 0 or (i - 3) % 7 == 0 :
            ten[i-1] = 1 

    for i in range(1,len(eleven)+1):
        if (i - 6) % 7 == 0 or i % 7 == 0 :
            eleven[i-1] = 1 

    for i in range(1,len(twelve)+1):
        if (i - 4) % 7 == 0 or (i - 5) % 7 == 0 :
            twelve[i-1] = 1 


    for i in holidays:
        if i.startswith('01') ==True :
            if i.startswith('0',3) == True:
                one[int(i[4])-1] = 1
            else:
                one[ (int(i[3])*10) + int(i[4]) - 1] = 1

        elif i.startswith('02') ==True :
            if i.startswith('0',3) == True:
                two[int(i[4])-1] = 1
            else:
                two[ (int(i[3])*10) + int(i[4]) - 1] = 1

        elif i.startswith('03') ==True :
            if i.startswith('0',3) == True:
                three[int(i[4])-1] = 1
            else:
                three[ (int(i[3])*10) + int(i[4]) - 1] = 1

        elif i.startswith('04') ==True :
            if i.startswith('0',3) == True:
                four[int(i[4])-1] = 1
            else:
                four[ (int(i[3])*10) + int(i[4]) - 1] = 1

        elif i.startswith('05') ==True :
            if i.startswith('0',3) == True:
                five[int(i[4])-1] = 1
            else:
                five[ (int(i[3])*10) + int(i[4]) - 1] = 1

        elif i.startswith('06') ==True :
            if i.startswith('0',3) == True:
                six[int(i[4])-1] = 1
            else:
                six[ (int(i[3])*10) + int(i[4]) - 1] = 1

        elif i.startswith('07') ==True :
            if i.startswith('0',3) == True:
                seven[int(i[4])-1] = 1
            else:
                seven[ (int(i[3])*10) + int(i[4]) - 1] = 1

        elif i.startswith('08') ==True :
            if i.startswith('0',3) == True:
                eight[int(i[4])-1] = 1
            else:
                eight[ (int(i[3])*10) + int(i[4]) - 1] = 1

        elif i.startswith('09') ==True :
            if i.startswith('0',3) == True:
                nine[int(i[4])-1] = 1
            else:
                nine[ (int(i[3])*10) + int(i[4]) - 1] = 1     
        
        elif i.startswith('10') ==True :
            if i.startswith('0',3) == True:
                ten[int(i[4])-1] = 1
            else:
                ten[ (int(i[3])*10) + int(i[4]) - 1] = 1        
        
        elif i.startswith('11') ==True :
            if i.startswith('0',3) == True:
                eleven[int(i[4])-1] = 1
            else:
                eleven[ (int(i[3])*10) + int(i[4]) - 1] = 1        

        elif i.startswith('12') ==True :
            if i.startswith('0',3) == True:
                twelve[int(i[4])-1] = 1
            else:
                twelve[ (int(i[3])*10) + int(i[4]) - 1] = 1           


        all_holy = one + two + three + four + five + six + seven + eight + nine + ten + eleven + twelve

        for i in all_holy:
            if i == 1:
                checker += 1
            elif i == 0:
                if checker != 0:
                    result.append(checker)
                    checker = 0
    result = set(result)            
    answer = list(result)
    answer.sort(reverse=True)
    print(answer)
    return answer[k-1]

holidays=["01/14","01/15","01/18","01/22","01/23","01/29","02/01","02/03","02/07"]
arr = solution(holidays, 2)
print(arr)
