function solution(N, stages) {
    const challenger = new Array(N + 2).fill(0);
    for (const stage of stages) {
        challenger[stage] += 1;
    }
    
    const fails = [];
    let total = stages.length;
    
    for (let i = 1; i <= N; i++){
        const failureRate = challenger[i] === 0 ? 0 : challenger[i] / total;
        fails.push([i, failureRate]);
        total -= challenger[i];
        
     }
    
    const result = fails.sort((a, b) => b[1] - a[1] || a[0] - b[0]).map(v => v[0]);
    
    return result;
}