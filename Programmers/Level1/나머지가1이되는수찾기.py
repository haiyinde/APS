def solution(n):
    x_candidates = list(range(1, n))
    for x in x_candidates:
        if n % x == 1:
            answer = x
            break

    return answer