array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count=[0]*(max(array)+1) # 최댓값 모두 담을 수 있도록하는 리스트 

print(count)

for i in range(len(array)):
  count[array[i]]+=1
print(count)

for i in range(len(count)):
  for j in range(count[i]):
    print(i,end=' ')
