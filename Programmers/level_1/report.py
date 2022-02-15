def solution(id_list, report, k):
    answer = []
    
    id = {}
    
    for name in id_list:
        id[name] = []
        
    new_report = set(report)
    report_count = {}
    for name in new_report:
        reporter , ban = name.split()
        
        id[reporter].append(ban)
        if ban not in report_count:
            report_count[ban] = 1
        else:
            report_count[ban] +=1
            
    for key , value in id.items():
        result = 0
        for name in value:
            if report_count[name] >= k :
                result += 1
        answer.append(result)
        
    return answer