# D2
import sys
sys.stdin = open("input.txt", "r")

last_day = {1: 31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
T = int(input())
for t in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    result = 0

    for i in range(m1, m2):
        result += last_day[i]

    result += d2 - d1 + 1

    print("#{} {}".format(t, result))