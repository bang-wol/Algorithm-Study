function solution(prices) {
    const stack = [];
        
    const times = new Array(prices.length).fill(0)
    
        for (let i=0; i<prices.length; i++) {
            while(stack.length > 0 && prices[stack[stack.length - 1]] > prices[i]) {
                const top = stack.pop();
                times[top] = i - top;
            }
            stack.push(i);
        }
    
    while (stack.length > 0) {
        const top = stack.pop();
        times[top] = prices.length -1 -top;
    }
    
    return times;
}