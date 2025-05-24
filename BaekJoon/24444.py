from collections import deque
import sys
input=sys.stdin.readline
n,m,p=map(int,input().split())
# 그래프 초기화 (1번부터 n번까지 사용하기 위해 n+1 크기)
graph = [[] for _ in range(n+1)]
cnt=1 # 방문순서
# 간선 정보 입력
for _ in range(m):
    u,v=list(map(int,input().split()))
    graph[u].append(v)
    graph[v].append(u)
print(graph)
# 방문 여부 저장 리스트
visited = [0] * (n + 1)#인덱스는 0부터 시작하는데 정점은 1부터 시작해서 인덱스 맞추려고 +1
#방문안했으면 False인거고 방문 했으면 True인거임
def bfs(V,E,R):
    queue = deque([R])#
    global cnt#방문순서
    visited[R] = cnt
    while queue:
        v=queue.popleft()
        #result.append(v)
        for i in sorted(V[v]):
            #False일때만 로직 수행해서 True일 떄는 pass임
            if not E[i]:#방문하지 않는 이웃만 큐에 넣기
                cnt+=1#몇 번째 방문했는지.
                E[i]=cnt
                queue.append(i)
    print(*E[1:])
bfs(graph,visited,p)


