n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cleaned = 0

while True:
    if graph[x][y] == 0:
        graph[x][y] = 2 # 청소 완료 표시
        cleaned += 1

    moved = False 
    
    for _ in range(4):
        d = (d + 3) % 4
        nx = x + dx[d]
        ny = y + dy[d]
        
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            x, y = nx, ny
            moved = True
            break
            
    if not moved:
        back = (d + 2) % 4 # 
        bx = x + dx[back]
        by = y + dy[back]
        
        if 0 <= bx < n and 0 <= by < m and graph[bx][by] != 1:
            x, y = bx, by 
        else:
            break

print(cleaned)        
