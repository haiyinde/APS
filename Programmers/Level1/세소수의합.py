from itertools import combinations


def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]


def solution(n):
    answer = 0
    cs = list(combinations(prime_list(n), 3))

    for c in cs:
        if sum(c) == n:
            answer += 1

    return answer