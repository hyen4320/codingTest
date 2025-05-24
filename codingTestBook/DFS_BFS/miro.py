from collections import deque

n,m = map(int,input().split())

#이동할 네 방향 정의 (상, 하 ,좌 ,우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def bfs(x,y):
    queue = deque()
    queue.append((x,y))#좌표를 큐에 집어넣음
    while queue:
        x,y=queue.popleft()
        #4방향으로 위치 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #미로찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx>=n or ny>=m:
                continue
            #벽인경우 무시
            if graph[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y]+1#
                queue.append((nx,ny))
                print(graph)
    #가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]
#1인경우 1을 더하여 거리를 표시함

print(bfs(0,0))