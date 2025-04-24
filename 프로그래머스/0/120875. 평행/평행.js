function solution(dots) {
    const line = (a, b) => (b[1] - a[1]) / (b[0] - a[0]);
    
    const [a, b, c, d] = dots;
    
    if (line(a, b) === line(c, d)) return 1;
    if (line(a, c) === line(b, d)) return 1;
    if (line(a, d) === line(b, c)) return 1;
    
    return 0;
}
