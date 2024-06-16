def solution(ineq, eq, n, m):
    comparison = ineq + eq
    
    if comparison == '>=':
        return 1 if n>=m else 0
    elif comparison == '<=':
        return 1 if n<=m else 0
    elif comparison == '>!':
        return 1 if n>m else 0
    elif comparison == '<!':
        return 1 if n<m else 0