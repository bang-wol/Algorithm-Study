T = int(input())

for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    sum=0
    for i in arr:
        if i%2!=0:
            sum+=i

    print(f'#{test_case} {sum}')
