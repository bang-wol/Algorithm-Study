N = int(input())
for i in range(1, N + 1):
    num_str = str(i)
    clap_count = num_str.count('3') + num_str.count('6') + num_str.count('9')

    if clap_count:
        print('-' * clap_count, end=" ")
    else:
        print(num_str, end=" ")
