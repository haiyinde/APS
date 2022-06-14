import sys

N = int(input())
words = set(sys.stdin.readline().strip() for _ in range(N))
words = list(words)
words.sort()
words.sort(key=len)

print(*words, sep="\n")