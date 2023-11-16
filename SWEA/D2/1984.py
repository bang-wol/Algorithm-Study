T=int(input())

for t in range(1,T+1):
  nums=list(map(int,input().split()))
  nums.sort()
  sum_nums=sum(nums[1:9])
  avg=round(sum_nums/8)
  print(f'#{t} {avg}')
