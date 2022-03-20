#D2
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    caseA = P * W

    if W <= R:
        caseB = Q
    else:
        caseB = Q + ( S * ( W-R ))

    print("#{} {}".format(t, min(caseA, caseB)))