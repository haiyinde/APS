def solution(numbers):
    zerotonine = list(range(0, 10))
    answer = 0
    for i in range(len(zerotonine)):
        if zerotonine[i] not in numbers:
            answer += zerotonine[i]
    return answer

# 효율적인 풀이
def solution1(numbers):
    return 45 - sum(numbers)