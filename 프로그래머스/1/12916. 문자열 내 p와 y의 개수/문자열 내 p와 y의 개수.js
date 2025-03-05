function solution(s){
    var answer = true;
    
    const lower = s.toLowerCase();
    
    const p = [...lower].filter((l)=> l==="p");
    const y = [...lower].filter((l)=> l==="y");

    if(p.length === y.length) {
        return true;
    } else {
        return false;
    }
}