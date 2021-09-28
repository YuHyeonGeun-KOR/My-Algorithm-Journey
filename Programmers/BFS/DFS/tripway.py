from collections import deque
def solution(tickets):
    answer = []
    airport = {}
    start_queue = deque()
    
    for ticket in tickets:
        airport[ticket[0]] =[]
    
    for ticket in tickets:
        airport[ticket[0]].append(ticket[1])
    
    start_queue.append("ICN")
    
    for i,j in airport.items():
        airport[i]  = sorted(airport[i] , reverse=True)
    print(airport)

    while start_queue:
        start = start_queue[-1]
        if start in airport and airport[start]:
            start_queue.append(airport[start].pop())    
        else:
            answer.append(start_queue.pop())

    
    answer.reverse()
    return answer