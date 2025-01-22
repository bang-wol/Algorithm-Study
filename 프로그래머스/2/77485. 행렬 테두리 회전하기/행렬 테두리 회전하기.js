function solution(rows, columns, queries) {
    const matrix = Array.from({ length: rows }, (_, i) =>
        Array.from({ length: columns }, (_, j) => i * columns + j + 1)
    );

    const answer = [];

    queries.forEach(([x1, y1, x2, y2]) => {
        const startX = x1 - 1;
        const startY = y1 - 1;
        const endX = x2 - 1;
        const endY = y2 - 1;

        let temp = matrix[startX][startY]; 
        let minVal = temp; 

        // 왼쪽 열 위로 이동
        for (let i = startX; i < endX; i++) {
            matrix[i][startY] = matrix[i + 1][startY];
            minVal = Math.min(minVal, matrix[i][startY]);
        }

        // 아래쪽 행 왼쪽으로 이동
        for (let i = startY; i < endY; i++) {
            matrix[endX][i] = matrix[endX][i + 1];
            minVal = Math.min(minVal, matrix[endX][i]);
        }

        // 오른쪽 열 아래로 이동
        for (let i = endX; i > startX; i--) {
            matrix[i][endY] = matrix[i - 1][endY];
            minVal = Math.min(minVal, matrix[i][endY]);
        }

        // 위쪽 행 오른쪽으로 이동
        for (let i = endY; i > startY + 1; i--) {
            matrix[startX][i] = matrix[startX][i - 1];
            minVal = Math.min(minVal, matrix[startX][i]);
        }

        matrix[startX][startY + 1] = temp;

        answer.push(minVal);
    });

    return answer;
}