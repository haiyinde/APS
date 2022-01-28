def solution(price, money, count):
    need = 0
    N = 1
    while count:
        count -= 1
        need += price * N
        N += 1
    answer = need - money
    if answer <= 0:
        answer = 0

    return answer


print(solution(3, 20, 4))