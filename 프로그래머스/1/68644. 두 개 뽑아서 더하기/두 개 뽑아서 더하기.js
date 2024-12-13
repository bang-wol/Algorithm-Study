function solution(numbers) {
    var answer = [];
    
    for(let n=0;n<numbers.length-1;n++){
        for(let m=n+1;m<numbers.length;m++){
            answer.push(numbers[n]+numbers[m])
        }
    }
    
    let result=[...new Set(answer)].sort((a,b)=>a-b);
    
    return result;
}