# 1984

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    numbers = sorted(list(map(int, input().split())))[1:-1]
    print("#{} {}".format(t, round(sum(numbers)/8)))

# 숏코딩 순위 들려고 변수명 줄여봄,,
# for t in range(1, int(input())+1):
#     print("#{} {}".format(t, round(sum(sorted(list(map(int, input().split())))[1:-1])/8)))
