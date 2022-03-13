# D2
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    numbers = sorted(list(map(int, input().split())))
    strings = [str(n) for n in numbers]
    print("#{} {}".format(t, " ".join(strings)))