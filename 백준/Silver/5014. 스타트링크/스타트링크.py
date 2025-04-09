from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [False] * (F + 1)

queue = deque()
queue.append((S, 0)) # 층, 버튼 누른 횟수 저장
visited[S] = True

while queue:
    current_floor, count = queue.popleft()
    
    if current_floor == G:
        print(count)
        break
        
    for next_floor in (current_floor + U, current_floor - D):
        if 1 <= next_floor <= F and not visited[next_floor]:
            visited[next_floor] = True
            queue.append((next_floor, count + 1))
            
else:
    print("use the stairs")

