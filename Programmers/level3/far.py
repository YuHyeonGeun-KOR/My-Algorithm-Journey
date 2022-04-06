from collections import deque
def solution(n, edge):
    answer = 0
    vertex = [[] for _ in range(n+1)]
    for e in edge :
        left , right = e[0] , e[1]
        vertex[left].append(right)
        vertex[right].append(left)
    
    queue = deque()
    queue.append([1,0])
    
    visited = [False] * len(vertex)
    visited[1] = True
    distance = {}
    
    while queue:
        now , dis = queue.popleft()
        flag = True
        for v in vertex[now]:
            if visited[v] == False: # 방문한적이 없는 노드면
                queue.append([v,dis+1]) # 큐우에 추가
                flag = False
                                    # 한번이라도 방문안한 노드를 만나면
                                    # flag 유지
            visited[v] = True

        if flag:
            if dis not in distance:
                distance[dis] = set()
            distance[dis].add(now)
                
    return len(distance[max(distance)])




n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,edge))