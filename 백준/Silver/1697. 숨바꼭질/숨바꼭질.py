from collections import deque

n, k = map(int, input().split())

MAX = 100001
dist = [0] * MAX

def bfs(start):
    queue = deque([start])
    while queue:
        x = queue.popleft()
        
        if x == k:
            print(dist[x])
            return
        
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX and dist[nx] == 0:
                dist[nx] = dist[x] + 1
                queue.append(nx)
                
bfs(n)       
