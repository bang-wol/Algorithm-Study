function solution(board) {
  const N = board.length;

  const danger = Array.from({ length: N }, () => Array(N).fill(0));

  const dx = [-1, -1, -1, 0, 0, 1, 1, 1];
  const dy = [-1, 0, 1, -1, 1, -1, 0, 1];

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (board[i][j] === 1) {
        danger[i][j] = 1; 

        for (let d = 0; d < 8; d++) {
          const ni = i + dx[d];
          const nj = j + dy[d];

            if (ni >= 0 && ni < N && nj >= 0 && nj < N) {
            danger[ni][nj] = 1;
          }
        }
      }
    }
  }

  let count = 0;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (danger[i][j] === 0) count++;
    }
  }

  return count;
}