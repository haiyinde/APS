# input에 \n도 포함되어있음 고려 필요
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set(input() for _ in range(N))
cnt = 0

for _ in range(M):
    t = input()
    if t in S:
        cnt += 1

print(cnt)