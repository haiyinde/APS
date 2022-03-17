# D2
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    _ = int(input())

    scores = list(map(int, input().split()))
    setted_scores = set(scores)

    result = {-1:-1}

    for i in setted_scores:
        tmp = scores.count(i)
        if tmp >= max(result.keys()):
            result[tmp] = i

    print(result)


    print("#{} {}".format(t, max(result.keys())))