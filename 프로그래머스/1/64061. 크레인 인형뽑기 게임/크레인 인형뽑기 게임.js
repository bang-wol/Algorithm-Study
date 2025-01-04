function solution(board, moves) {
  const stack = []; 
  let count = 0;   

  for (let move of moves) {
    const col = move - 1; 

    for (let row = 0; row < board.length; row++) {
      if (board[row][col] !== 0) {
        const doll = board[row][col]; 
        board[row][col] = 0; 

        if (stack.length > 0 && stack[stack.length - 1] === doll) {
          stack.pop(); 
          count += 2;  
        } else {
          stack.push(doll); 
        }
        break; 
      }
    }
  }

  return count;
}
