from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def melt():
    temp = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if graph[x][y] > 0:
                sea = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                        sea += 1
                temp[x][y] = max(0, graph[x][y] - sea)
    return temp

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] > 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
year = 0

while True:
    visited = [[False] * m for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                count += 1
    
    if count == 0:
        print(0)
        break
    
    if count >= 2:
        print(year)
        break
    
    graph = melt()
    year += 1
    
           