#너비우선탐색 솔루션입니다.
#위=>오른쪽=>아래쪽=>왼쪽
gap_x = [0,1,0,-1]
gap_y = [-1,0,1,0]
def backtracking(maze,ex,ey):
  foots=[]#백트래킹에 사용할 컬렉션 생성
  foots.append([ex,ey])
  foot = maze[ey][ex]
  now_x = ex
  now_y = ey
  while foot>2: #출발지 이전 좌표를 만나기 전까지    (현재 좌표에서 이전 좌표를 찾아서 경로에 추가하기 때문에)
    for di in range(4): #위=>오른쪽=>아래쪽=>왼쪽
      before_x = now_x + gap_x[di]
      before_y = now_y + gap_y[di]
      if maze[before_y][before_x] == foot-1: #이전 경로일 때
        foots.append([before_x,before_y])
        now_x = before_x
        now_y = before_y
        foot = maze[now_y][now_x]
        break#반드시 루프 탈출
  foots.reverse()#역순으로 배치
  return foots
def loadofflood(maze,sx,sy):
  queue=[]#비어있는 큐 생성
  queue.append([sx,sy])#시작 좌표를 큐에 보관
  while(len(queue)>0):#반복 - 큐가 비어있지 않다면
    now_x,now_y = queue.pop(0)#현재 좌표 := 큐에서 꺼내온다.
    foot = maze[now_y][now_x]#foot:= 맵에 쓰여진 값
    for di in range(4):#반복 - 위=>오른쪽=>아래쪽=>왼쪽
      next_x = now_x + gap_x[di]
      next_y = now_y + gap_y[di]#다음 좌표:= 현재 좌표에서 해당 방향을 고려한 값
      if maze[next_y][next_x] == -2:#조건 - 다음 좌표가 목적지일 때
        maze[next_y][next_x] = foot + 1#맵의 다음 좌표에 foot+1을 마킹
        return backtracking(maze,next_x, next_y)#backtracking한 결과를 반환
      elif maze[next_y][next_x] == 0:#길일 때
        maze[next_y][next_x] = foot + 1#맵의 다음 좌표에 foot+1을 마킹
        queue.append([next_x,next_y])#큐에 다음 좌표를 보관
  return []#길이 없다.[]반환

maze = [
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1, 1, 0, 0, 0, 0,-1, 0, 0, 0, 0,-1],
    [-1, 0,-1,-1, 0,-1, 0,-1, 0,-1, 0,-1],
    [-1, 0,-1,-1, 0,-1, 0, 0, 0,-1, 0,-1],
    [-1, 0,-1, 0, 0, 0, 0,-1,-1, 0, 0,-1],
    [-1, 0,-1, 0,-1,-1, 0,-1, 0,-1,-1,-1],
    [-1, 0,-1,-1, 0,-1, 0, 0, 0, 0, 0,-1],
    [-1, 0,-1, 0, 0,-1, 0,-1, 0,-1, 0,-1],
    [-1, 0, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1],
    [-1, 0,-1,-1,-1, 0, 0,-1, 0, 0, 0,-1],
    [-1, 0, 0, 0,-1,-1,-1, 0, 0,-1,-2,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        ]
path = loadofflood(maze,1,1)        
print(path)