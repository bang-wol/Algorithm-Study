import sys
sys.stdin = open("1859.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    max_price = prices[-1]
    profit = 0

    for i in range(N-2, -1, -1):
        if prices[i] < max_price:
            profit += max_price - prices[i]
        else:
            max_price = prices[i]

    print(f'#{test_case} {profit}')
