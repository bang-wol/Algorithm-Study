function solution(s) {
    let count = 0;
    const n = s.length;
    
    for (let i=0; i<n; i++) {
        const stack = [];
        const rotated = s.slice(i) + s.slice(0, i);
        let isCorrect = true;
        
        for (let char of rotated) {
            if (char === '(' || char === '{' || char === '[') {
                stack.push(char);
            } else {
                const top = stack.pop();
                if(
                    (char === ')' && top !== '(') ||
                    (char === '}' && top !== '{') ||
                    (char === ']' && top !== '[')    
                ) {
                    isCorrect = false;
                    break;
                }
            }
        }
        
        if (isCorrect && stack.length === 0) {
            count++;
        }
    }
    return count;
}