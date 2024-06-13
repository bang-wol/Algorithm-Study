def solution(a, b):
    answer = ''
    
    answer=str(a)+str(b)
    
    
    if int(str(b)+str(a))>int(answer):
        return int(str(b)+str(a))
        
    return int(answer)