def solution(genres, plays):
    answer = []

    music = []
    c = {}
    sum_c = {} 
    for i in range(0,len(genres)):
        music.append(  [  genres[i],[i,plays[i]] ]   )

    for i in range(0,len(genres)):
        try : 
            c[music[i][0]].append(music[i][1])
            sum_c[music[i][0]] +=  music[i][1][1]
        except : 
            c[music[i][0]] = [music[i][1]]
            sum_c[music[i][0]] = music[i][1][1]
    
    c_sort = []
    
    for i in c.items():
        c_sort.append(i)
    
    sum_c_sort = sorted(sum_c.items(), key = lambda x : (x[1]))
    sum_c_sort.reverse()
    

    for i in c_sort:
        i[1].sort(key=lambda x: x[1]) 
        i[1].reverse()

    for i in range(len(sum_c_sort)):
        for j in range(len(c_sort)):
            if sum_c_sort[i][0] == c_sort[j][0] and len(c_sort[j][1]) >=2:
                if c_sort[j][1][0][1] == c_sort[j][1][1][1] and c_sort[j][1][0][0] < c_sort[j][1][1][0]:
                    answer.append(c_sort[j][1][0][0])
                    answer.append(c_sort[j][1][1][0])
                elif c_sort[j][1][0][1] == c_sort[j][1][1][1] and c_sort[j][1][0][0] > c_sort[j][1][1][0]:
                    answer.append(c_sort[j][1][1][0])
                    answer.append(c_sort[j][1][0][0])
                else:
                    answer.append(c_sort[j][1][0][0])
                    answer.append(c_sort[j][1][1][0])
            elif sum_c_sort[i][0] == c_sort[j][0] and len(c_sort[j][1]) == 1:
                answer.append(c_sort[j][1][0][0])
            

    return answer