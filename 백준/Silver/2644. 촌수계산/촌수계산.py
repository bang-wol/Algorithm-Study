from collections import deque

n = int(input()) # 전체 사람 수 
a, b = map(int, input().split()) # 촌수 계산할 두 사람
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
visited = [False] * (n + 1)
dist = [0] * (n + 1) # 촌수 저장

def bfs(start):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        now = queue.popleft()
        
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                dist[next] = dist[now] + 1
                queue.append(next)

bfs(a)

print(dist[b] if visited[b] else -1)
    