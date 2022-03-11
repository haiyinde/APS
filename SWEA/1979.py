# D2
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(input().split()) for _ in range(N)]
    cnt = 0
    for r in puzzle:
        line = "".join(r).split("0")
        cnt += line.count("1"*K)

    for c in zip(*puzzle):
        line = "".join(c).split("0")
        cnt += line.count("1"*K)

    print("#{} {}".format(t, cnt))