function solution(maps) {
    const directions = [
        [1, 0], [-1, 0], [0, 1], [0, -1]
    ];
    const rows = maps.length;
    const cols = maps[0].length;

    const bfs = (startX, startY, target) => {
        const queue = [[startX, startY, 0]];
        const visited = Array.from({ length: rows }, () => Array(cols).fill(false));
        visited[startX][startY] = true;

        while (queue.length > 0) {
            const [x, y, steps] = queue.shift();

            if (maps[x][y] === target) return [x, y, steps];

            for (const [dx, dy] of directions) {
                const nx = x + dx;
                const ny = y + dy;

                if (
                    nx >= 0 && nx < rows &&
                    ny >= 0 && ny < cols &&
                    !visited[nx][ny] &&
                    maps[nx][ny] !== "X"
                ) {
                    visited[nx][ny] = true;
                    queue.push([nx, ny, steps + 1]);
                }
            }
        }

        return [-1, -1, -1];
    };

    let startX, startY;
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (maps[i][j] === "S") {
                startX = i;
                startY = j;
            }
        }
    }

    const lever = bfs(startX, startY, "L");
    if (lever[2] === -1) return -1;

    const exit = bfs(lever[0], lever[1], "E");
    if (exit[2] === -1) return -1;

    return lever[2] + exit[2];
}