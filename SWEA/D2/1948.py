# D2
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    result = 0

    for i in range(m1, m2):
        result += last_day[i]

    result += d2 - d1 + 1

    print("#{} {}".format(t, result))