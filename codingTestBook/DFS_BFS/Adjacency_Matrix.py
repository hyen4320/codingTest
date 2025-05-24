INF=999999999 # 무한의 비용 선언
#2차원 리스트를 이용해 인접 행렬 표현
graph=[
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]
print(graph)

graph = [[] for _ in range(3)]
graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((1,5))

print(graph)