def dfs(graph,v,visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v,end=' ')

    for i in graph[v]:
        if not visited[i]:#방문을 하지 않은 것을 먼저 탐색
            dfs(graph,i,visited)
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9

dfs(graph,1,visited)
