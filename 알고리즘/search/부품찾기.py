def binary_search(array,target,start,end):
  while start<=end:
    mid=(start+end)//2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid]==target:
      return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid]>target:
      end=mid-1
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
    else:
      start=mid+1  
  return None
  
n=int(input())
have=list(map(int(input().split()))) # 매장에 있는 부품
have.sort()

m=int(input())
buy=list(map(int(input().split()))) # 손님이 문의한 부품

# 부품 하나씩 확인
for i in buy:
  result=binary_search(have,i,0,n-1)
  
  if result!=None:
    print('yes',end=' ')
  else:
    print('no',end=' ')

