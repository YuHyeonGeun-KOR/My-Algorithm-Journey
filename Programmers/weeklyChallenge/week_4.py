def solution(table, languages, preference):
    answer = ''
    company_tables={}
    comName = []
    for company in table:
        com_list = company.split()
        
        rank = {}
        comName.append(com_list[0])
        s_set = 5
        for i in range(1,len(com_list)):
            rank[com_list[i]] = s_set
            s_set-=1
        company_tables[comName[-1]] = rank
        
    result = {}
    for company_table in company_tables:
        idx =0
        score_sum = 0
        
        for i in range(len(languages)):
            if languages[i] in company_tables[company_table]:
                score_sum += preference[i] * company_tables[company_table][languages[i]]
        idx +=1
        result[company_table] = score_sum
    
    result= sorted(result , key = lambda x : (-result[x],x))
    
    return result[0]


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]
print(solution(table,languages, preference))