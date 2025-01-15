function solution(orders, course) {
    const getCombinations = (arr, length) => {
        if (length === 1) return arr.map(item => [item]);
        const result = [];
        arr.forEach((fixed, index, origin) => {
            const rest = origin.slice(index + 1);
            const combinations = getCombinations(rest, length - 1);
            const attached = combinations.map(combo => [fixed, ...combo]);
            result.push(...attached);
        });
        return result;
    };
    
    var answer = [];
    
    course.forEach(length => {
        const comboCount = new Map();
        
        orders.forEach(order => {
            const sortedOrder = order.split('').sort();
            const combinations = getCombinations(sortedOrder, length);
            
            combinations.forEach(combo => {
                const comboKey = combo.join('');
                comboCount.set(comboKey, (comboCount.get(comboKey) || 0) + 1);
            });
        });
        
        const maxCount = Math.max(...comboCount.values(), 2);
        comboCount.forEach((count, key) => {
            if (count === maxCount && count > 1) {
                answer.push(key);
            }
        });
    });
    
    return answer.sort();
}