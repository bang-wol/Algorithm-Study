from collections import deque

def solution(priorities, location):
    answer = 0
    queue=deque([(priority,idx) for idx,priority in enumerate(priorities)])
    
    while queue:
        current=queue.popleft()
        if any(current[0]<item[0] for item in queue):
            queue.append(current)
        else:
            answer+=1
            if current[1]==location:
                return answer
    
    return answer


