n=int(input())
users=[]

index=0
for _ in range(n):
    age, name=input().split()
    users.append((int(age), name, index))
    index+=1

users.sort(key=lambda user:(user[0],user[2]))

for user in users:
    print(user[0],user[1])