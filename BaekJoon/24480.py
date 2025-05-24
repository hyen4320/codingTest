import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
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

def dfs(V,E,R):
    global cnt
    E[R] = cnt  # 방문 순서 저장
    
    for i in sorted(V[R],reverse=True):
        if E[i]==0:
            cnt+=1#방문했을 떄만 카운트 올리기
            dfs(V,E,i)

dfs(graph,visited,p)
#24일 재귀로 구현하기
print(*visited[1::])


