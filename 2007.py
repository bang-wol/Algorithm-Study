T = int(input())

for t in range(1, T + 1):
    string = input()

    for i in range(1, 11):
        if string[:i] == string[i:2*i]:
            print(f"#{t} {i}")
            break
