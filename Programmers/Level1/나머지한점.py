from collections import defaultdict


def solution(v: list):
    answer = [0, 0]
    xdict = defaultdict(int)
    ydict = defaultdict(int)

    for c in v:
        x, y = c[0], c[1]
        xdict[x] += 1
        ydict[y] += 1

    for xk, xv in xdict.items():
        if xv % 2 != 0:
            answer[0] = xk
    for yk, yv in ydict.items():
        if yv % 2 != 0:
            answer[1] = yk

    return answer