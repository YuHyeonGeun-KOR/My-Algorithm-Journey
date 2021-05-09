from collections import deque
def bfs(x,y,visited,checker_list):
    queue = deque()
    queue.append((x,y))
    distance = [[0]* 5 for _ in range(5)]
    distance[x][y] = 1
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    flag = 1
    while queue:
        x,y=queue.popleft()

        for i in range (4):
            xx = x + dx[i]
            yy = y + dy[i]

            if  xx <= -1 or xx >= 5 or  yy <= -1 or yy >= 5 or  distance[xx][yy] ==1:
                continue 
            elif checker_list[xx][yy] == 'O' :
                visited[xx][yy] = visited[x][y] + 1 
                distance[xx][yy] = 1
                queue.append((xx,yy))
            elif checker_list[xx][yy] == 'P' :
                visited[xx][yy] = visited[x][y] + 1 
                distance[xx][yy] = 1
                if visited[xx][yy] <= 2:
                    flag = 0
                    return flag
                queue.append((xx,yy))

    return flag
def solution(places):
    answer = []
    place_one = places[0]
    place_two = places[1]
    place_three = places[2]
    place_four = places[3]
    place_five = places[4]
    
    place_one_list =[]
    place_two_list =[]
    place_three_list =[]
    place_four_list =[]
    place_five_list =[]

    place_one_player =[]
    place_two_player =[]
    place_three_player =[]
    place_four_player =[]
    place_five_player =[]

    for i in place_one:
        place_one_list.append(list(i))
    for i in place_two:
        place_two_list.append(list(i))
    for i in place_three:
        place_three_list.append(list(i))
    for i in place_four:
        place_four_list.append(list(i))
    for i in place_five:
        place_five_list.append(list(i))

    one=1
    two=1
    three=1
    four=1
    five=1

    for i in range(5):
        for j in range(5):
            if place_one_list[i][j] == 'P':
                place_one_player.append([i,j])

    for i in range(5):
        for j in range(5):
            if place_two_list[i][j] == 'P':
                place_two_player.append([i,j])

    for i in range(5):
        for j in range(5):
            if place_three_list[i][j] == 'P':
                place_three_player.append([i,j])

    for i in range(5):
        for j in range(5):
            if place_four_list[i][j] == 'P':
                place_four_player.append([i,j])

    for i in range(5):
        for j in range(5):
            if place_five_list[i][j] == 'P':
                place_five_player.append([i,j])      

   

    for i in place_one_player:
        visited = [[0]* 5 for _ in range(5)]
        
        if bfs(i[0],i[1],visited,place_one_list) == 0:
            one = 0
            break
        

    for i in place_two_player:
        visited = [[0]* 5 for _ in range(5)]
        
        if bfs(i[0],i[1],visited,place_two_list) == 0:
            two = 0
            break
        


    for i in place_three_player:
        visited = [[0]* 5 for _ in range(5)]
        
        if bfs(i[0],i[1],visited,place_three_list) == 0:
            three =0
            break
       

    for i in place_four_player:
        visited = [[0]* 5 for _ in range(5)]
        if bfs(i[0],i[1],visited,place_four_list) == 0:
            four =0
            break
       


    for i in place_five_player:
        visited = [[0]* 5 for _ in range(5)]
         
        if bfs(i[0],i[1],visited,place_five_list) == 0:
            five =0
            break



    answer.append(one)
    answer.append(two)
    answer.append(three)
    answer.append(four)
    answer.append(five)

    return answer


    

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
         ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
         ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], 
         ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))