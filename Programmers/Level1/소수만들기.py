from itertools import combinations

def isPrimeNumber(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


def solution(nums):
    answer = 0
    cs = list(combinations(nums, 3))
    for c in cs:
        if isPrimeNumber(sum(c)):
            answer += 1

    return answer