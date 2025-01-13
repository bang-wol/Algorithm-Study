function solution(record) {
    var answer = [];
    const recordMap = new Map();
    
    for (const r of record) {
        const [state, userId, nickName] = r.split(' ');
        
        if (state === 'Enter' || state === 'Change') {
            recordMap.set(userId, nickName)
        }
    }
    
    for (const r of record) {
        const [state, userId] = r.split(' ');
        
        if(state === 'Enter') {
            answer.push(recordMap.get(userId)+'님이 들어왔습니다.')
        } else if(state === 'Leave') {
            answer.push(recordMap.get(userId)+'님이 나갔습니다.')
        }
    }
    
    return answer;
}