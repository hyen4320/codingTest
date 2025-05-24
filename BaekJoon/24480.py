###입력값
n,m,p=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
cnt=1
###인접리스트 방식#연결정보를 표현해야해서 m이 맞음. m이 간선의 수임
for i in range(m):
    x,y=map(int,input().split())
    graph[y].append(x)
    graph[x].append(y)

print(graph)
#24일 재귀로 구현하기


