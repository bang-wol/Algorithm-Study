from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M): # 간선 정보 M개 저장, a <-> b 양방향 그래프
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, N+1): # 정점 번호가 작은 것부터 방문하도록 정렬
    graph[i].sort()
    
def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)

def bfs(start):
    visited = [False] * (N+1)
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                
visited = [False] * (N+1)
dfs(V, visited)

print()

bfs(V)
