import sys

input = sys.stdin.readline

def solution(scores):
    answer = ''
    avg = 0 

    for i in range(len(scores)):
        isOnlyMaxNum = True
        isOnlyMinNum = True
        total = 0 
        self_Num = scores[i][i]  

        for j in range(len(scores)):
            total += scores[j][i]
            if i == j :
                continue
            else:
                if scores[j][i] >= self_Num:
                    isOnlyMaxNum = False
                if scores[j][i] <= self_Num:
                    isOnlyMinNum = False
                


        if isOnlyMaxNum or isOnlyMinNum :
            avg = (total - self_Num) / (len(scores) - 1) 
        else: 
            avg = total / len(scores)

        
          
    

    
    


        if avg >= 90 :
            answer += 'A'
        elif 80 <= avg < 90 :
            answer += 'B'
        elif 70 <= avg < 80:
            answer += 'C'
        elif 50 <= avg < 70:
            answer += 'D'
        else:
            answer += 'F' 

    return answer

scores =[[100,100],[100,100]]

print(solution(scores))