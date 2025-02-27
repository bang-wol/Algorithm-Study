function solution(s, skip, index) {
    const skipSet = new Set(skip); 
    let result = '';

    for (let char of s) {
        let count = 0;
        let currentCharCode = char.charCodeAt(0); 

        while (count < index) {
            currentCharCode++; 

            if (currentCharCode > 'z'.charCodeAt(0)) {
                currentCharCode = 'a'.charCodeAt(0);
            }

            if (!skipSet.has(String.fromCharCode(currentCharCode))) {
                count++;
            }
        }
        
        result += String.fromCharCode(currentCharCode);
    }

    return result;
}