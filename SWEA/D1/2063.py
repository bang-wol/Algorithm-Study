N = int(input())
num = list(map(int,input().split()))
num.sort()
mid_num=num[(N-1)//2]
print(mid_num)
