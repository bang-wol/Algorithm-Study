T=int(input())

for t in range(1,T+1):
    N,M=map(int,input().split())
    grid=[list(map(int,input().split())) for _ in range(N)]
    max_flies=0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total_fly=sum(grid[x][y] for x in range(i,i+M) for y in range(j,j+M))
            max_flies=max(max_flies, total_fly)

    print(f'#{t} {max_flies}')
