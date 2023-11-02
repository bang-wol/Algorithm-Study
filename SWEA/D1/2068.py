T = int(input())

for test_case in range(1, T+1):
    arr = list(map(int,input().split()))
    max_num = max(arr)
    print(f'#{test_case} {max_num}')
