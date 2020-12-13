def solution(answers):
    answer = []
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    s1 = 0
    s2 = 0
    s3 = 0
    for i in range(len(answers)):
        if a1[i%5]==answers[i]:
            s1+=1
        if a2[i%8]==answers[i]:
            s2+=1
        if a3[i%10]==answers[i]:
            s3+=1
    M = max(s1,(max(s2,s3))) 
    if M == s1:
        answer.append(1)
    if M == s2:
        answer.append(2)
    if M == s3:
        answer.append(3)
    
    return answer