import sys
input=sys.stdin.readline
n=int(input())
m=int(input())

graph=[[] for _ in range(n+1)]

visited=[False] * (n+1)

for i in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
def virus(graph,visited,p):
    visited[p]=True#진입 시 한 번만 수행
    for i in graph[p]:
        if not visited[i]:
            
            virus(graph=graph,visited=visited,p=i)
virus(graph=graph,visited=visited,p=1)
print(visited.count(True)-1)
