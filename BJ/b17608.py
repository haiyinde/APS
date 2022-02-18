# Stack, B2
import sys
input = sys.stdin.readline

N = int(input())
sticks = [int(input()) for _ in range(N)]

highest = 0
cnt = 0

for i in range(len(sticks)-1, -1, -1):
    if highest < sticks[i]:
        highest = sticks[i]
        cnt += 1

print(cnt)
