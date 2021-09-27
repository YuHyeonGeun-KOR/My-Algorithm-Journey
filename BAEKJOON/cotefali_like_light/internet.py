import sys
import heapq
input = sys.stdin.readline

n,p,k = map(int, input().split())

INF = 1e9
graph = [[] for i in range(n+1)]
#방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
#최단거리 테이블을 모두 무한으로 초기화
distance =[INF] * (n+1)
for i in range(p):
    left ,right , cost = map(int, input().split())
    graph[left].append((right,cost))
    graph[right].append((left,cost))
print(graph)
def dijkstra(start):
    q = []
  #시작 노드로 가기 위한 최단 경로는 0 으로 설정하며 , 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:#큐가 비어 있지 않다면
    #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist , now = heapq.heappop(q)
    #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] <dist:
            continue
    #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
      #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(1)
print(distance)