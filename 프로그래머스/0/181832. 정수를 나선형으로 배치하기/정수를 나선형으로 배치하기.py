def solution(n):
    answer = [[0]*n for _ in range(n)]
    
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    current_direction =0
    
    row, col =0,0
    for i in range(1, n*n+1):
        answer[row][col]=i
        next_row=row+directions[current_direction][0]
        next_col=col+directions[current_direction][1]
        
        if next_row <0 or next_row >=n or next_col <0 or next_col>=n or answer[next_row][next_col]!=0:
            current_direction=(current_direction+1)%4
            next_row=row+directions[current_direction][0]
            next_col=col+directions[current_direction][1]
        row, col=next_row, next_col
        

    
    return answer