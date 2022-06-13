import sys
input = sys.stdin.readline

N, M = map(int, input().split())

not_heard = set(input().strip() for _ in range(N))
not_seen = set(input().strip() for _ in range(M))

not_heard_seen = list(not_heard & not_seen)

print(len(not_heard_seen))
print(*sorted(not_heard_seen), sep="\n")
