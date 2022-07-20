from itertools import combinations

def solution(m, weights):
    cs = []
    for i in range(len(weights)):
        c = list(combinations(weights, i))
        cs.extend(c)

    return [sum(c) for c in cs].count(m)