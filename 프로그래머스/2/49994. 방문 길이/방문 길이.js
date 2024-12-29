function solution(dirs) {
    const isValidMove = (nx, ny) => nx >= -5 && nx <=5 && ny >= -5 && ny <=5;
    
    const move = {
        'U': (x, y) => [x, y+1],
        'D': (x, y) => [x, y-1],
        'R': (x, y) => [x+1, y],
        'L': (x, y) => [x-1, y],
    };
    
    let x = 0, y = 0;
    
    const visited = new Set();
    
    for (const dir of dirs){
        const [nx, ny] = move[dir](x, y);
        
        if(!isValidMove(nx, ny)){
            continue;
        }
        
        visited.add(`${x}${y}${nx}${ny}`);
        visited.add(`${nx}${ny}${x}${y}`);
        
        [x, y] = [nx, ny];
    }
    
    return visited.size / 2;
}