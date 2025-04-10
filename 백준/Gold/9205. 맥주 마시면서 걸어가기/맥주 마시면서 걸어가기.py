from collections import deque

def bfs():
    queue = deque()
    queue.append(0)
    visited[0] = True
    
    while queue:
        now =  queue.popleft()
        
        if now == n + 1:
            return "happy"
        
        for next in range(n + 2):
            if not visited[next]:
                dist = abs(pos[now][0] - pos[next][0]) + abs(pos[now][1] - pos[next][1])
                if dist <= 1000:
                    visited[next] = True
                    queue.append(next)
                    
    return "sad"

t = int(input())
for _ in range(t):
    n = int(input())
    pos = []
    
    for _ in range(n + 2):
        x, y = map(int, input().split())
        pos.append((x, y))
        
    visited = [False] * (n + 2)
    print(bfs())
