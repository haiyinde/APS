def solution(left, right):
    numbers = list(range(left, right + 1))

    answer = 0

    for num in numbers:
        common_divisor = 0
        for i in range(1, num + 1):
            if num % i == 0:
                common_divisor += 1
        if common_divisor % 2 == 0:  # 짝수이면
            answer += num
        elif common_divisor % 2 == 1:  # 홀수이면
            answer -= num

    return answer