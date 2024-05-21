def solution(progresses, speeds):
    from math import ceil
    answer = []

    days=[ceil((100-p)/s) for p,s in zip(progresses, speeds)]
    
    while days:
        current_day=days.pop(0)
        count=1
        
        while days and days[0]<=current_day:
            days.pop(0)
            count+=1
            
        answer.append(count)
    
    return answer