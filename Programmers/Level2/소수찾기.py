from itertools import permutations


def isPrime(n):
    if n == 0 or n == 1:
        return False

    if n == 2 or n == 3:
        return True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    for i in range(1, len(numbers) + 1):
        p = list(permutations(numbers, i))
        for j in range(len(p)):
            num = int("".join(map(str, p[j])))  # 튜플 처리
            if isPrime(num):
                answer.append(num)
    answer = list(set(answer))

    return len(answer)