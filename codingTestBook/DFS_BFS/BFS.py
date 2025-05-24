from collections import deque

def bfs(graph, start, visited):
    #Queue 구현을 위한 collections deque
    queue = deque([start])
    #현재 노드를 방문 처리
    visited[start]=True
    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v=queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
            
graph=[
    [],#0번 정점
    [2,3,8],#1번정점과 연결된 정점
    [1,7],#2번 정점과 연결된 정점
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9
bfs(graph=graph,start=1, visited=visited)