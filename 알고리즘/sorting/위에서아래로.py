n=int(input())

array=[]
for i in range(n):
  array.append(int(input()))

array=sorted(array, reverse=True) # list.sort() 함수는 리턴 값 none !

for i in array:
  print(i,end=" ")
