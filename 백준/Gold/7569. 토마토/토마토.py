from collections import deque

m, n, h = map(int, input().split())
graph = [[[0] * m for _ in range(n)] for _ in range(h)]

for z in range(h):
    for y in range(n):
        graph[z][y] = list(map(int, input().split()))

dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

queue = deque()

# 익은 토마토 좌표 큐에 미리 담아놓기
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                queue.append((z, x, y))
                
while queue:
    z, x, y = queue.popleft()
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz, nx, ny))

result = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 0:
                print(-1)
                exit()
            result = max(result, graph[z][x][y])

print(result - 1)
               