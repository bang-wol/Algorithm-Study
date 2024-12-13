function solution(answers) {
    var answer = [];
    
    const supozas=[
        {
            id:1,
            pattern:[1,2,3,4,5],
            count:0
        },
         {
            id:2,
            pattern:[2,1,2,3,2,4,2,5],
            count:0
        }, {
            id:3,
            pattern:[3,3,1,1,2,2,4,4,5,5],
            count:0
        },
    ]

    for(let i=0; i<answers.length; i++){
        for(let j=0;j<supozas.length;j++){
            if(answers[i]===supozas[j].pattern[i%supozas[j].pattern.length]){
                supozas[j].count++;
            };

        }
    }
        
    const maxCount=Math.max(...supozas.map(s=>s.count));
    
    answer=supozas
    .filter(s=>s.count===maxCount)
    .map(s=>s.id)
    .sort((a,b)=>a-b);
    
    return answer;
}