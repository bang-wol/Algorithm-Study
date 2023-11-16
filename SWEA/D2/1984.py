T=int(input())

for t in range(1,T+1):
  num=list(map(int,input().split()))
  max_num=max(num)
  min_num=min(num)
  num.remove(max_num)
  num.remove(min_num)
  avg=round(sum(num)/len(num))
  print(f'#{t} {avg}')
