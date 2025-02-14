function solution(citations) {
    let h = 0;
    
    citations.sort((a, b)=> b - a);
    
    for (let n = 0; n < citations.length; n++) {
        if (citations[n] >= n + 1) {
            h = n + 1;
        } else {
            break;
        }
    }
    
    return h;   
}