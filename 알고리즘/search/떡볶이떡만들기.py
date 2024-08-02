n,m=list(map(int(input()).split(' ')))
array=list(map(int(input().split())))

# 시작점, 끝점 설정
start=0
end=max(array)
result=0

# 이진 탐색 수행(재귀x 반복적)
while(start<=end):
  total=0
  mid=(start+end)//2
  for x in array:
    if x>mid:
      total+=x-mid
  if total <m:
    end = mid -1
  else:
    result=mid
    start=mid+1  

print(result)