# D2
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    h3, m3 = h1+h2, m1+m2
    if h3 >= 13:
        h3 = h3 % 12
    if m3 >= 61:
        h3 += 1
        m3 = m3 % 60
    print("#{} {} {}".format(t, h3, m3))