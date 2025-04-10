from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 빨간 구슬, 파란 구슬 위치 찾기
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

# 구슬을 한 방향으로 끝까지 굴리는 함수
def move(x, y, dx, dy):
    count = 0  # 이동 거리 (누가 먼저 도착했는지 비교용)
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

# 방문 여부 저장 [rx][ry][bx][by]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
visited[rx][ry][bx][by] = True

queue = deque()
queue.append((rx, ry, bx, by, 0))

while queue:
    rx, ry, bx, by, depth = queue.popleft()

    if depth >= 10:
        break

    for i in range(4):
        nrx, nry, rc = move(rx, ry, dx[i], dy[i])
        nbx, nby, bc = move(bx, by, dx[i], dy[i])

        # 파란 구슬이 구멍에 빠지면 → 실패
        if board[nbx][nby] == 'O':
            continue

        # 빨간 구슬만 구멍에 빠지면 → 성공
        if board[nrx][nry] == 'O':
            print(depth + 1)
            sys.exit()

        # 겹쳤으면 더 늦게 온 애를 한 칸 뒤로
        if nrx == nbx and nry == nby:
            if rc > bc:
                nrx -= dx[i]
                nry -= dy[i]
            else:
                nbx -= dx[i]
                nby -= dy[i]

        # 아직 방문 안 했으면 큐에 넣기
        if not visited[nrx][nry][nbx][nby]:
            visited[nrx][nry][nbx][nby] = True
            queue.append((nrx, nry, nbx, nby, depth + 1))

print(-1)  # 10번 안에 못 빼내면 실패