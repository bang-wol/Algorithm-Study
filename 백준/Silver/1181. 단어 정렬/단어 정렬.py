n=int(input())
words=set(input() for _ in range(n))

sorted_words=sorted((len(word),word) for word in words)

for length, word in sorted_words:
    print(word)