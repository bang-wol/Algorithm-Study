P, K = map(int, input().split())
if P >= K:
    attempt_count = P - K + 1
else:
    attempt_count = 1000 - K + P + 1
print(attempt_count)
