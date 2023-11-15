T=int(input())

for test_case in range(1,T+1):
    N=int(input())
    triangle=[[1]]

    for i in range(1,N):
        row=[1]
        for j in range(1,i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    print(f'#{test_case}')
    for row in triangle:
        print(' '.join(map(str,row)))
