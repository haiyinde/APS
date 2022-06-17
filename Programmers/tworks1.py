def solution(p):
    n: int = len(p)
    answer: list = [0] * n

    for i in range(n):
        pj: int = min(p[i:])
        j: int = p.index(pj)

        if i != j:
            p[i], p[j] = p[j], p[i]
            answer[i] += 1
            answer[j] += 1
        i += 1

        if i < n:
            continue

        if i == j:
            break

    return answer

print(solution([2, 5, 3, 1, 4]))
print(solution([2, 3, 4, 5, 6, 1]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))