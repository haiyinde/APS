# D2
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    zipped = {}
    for _ in range(N):
        tmp1, tmp2 = input().split()
        zipped[tmp1] = int(tmp2)

    print("#{}".format(t))

    result = []

    for key, value in zipped.items():
        for i in range(value):
            result.append(key)

    L = sum(zipped.values())//10 + 1

    for i in range(L):
        print("".join(result[i*10:i*10+10]))