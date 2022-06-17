def check_vip(period: int, total: int):
    if total >= 900000 and period >= 24:
        return True
    elif total >= 600000 and period >= 60:
        return True
    return False


def solution(periods: list, payments: list, estimates: list):
    answer = [0, 0]
    n = len(periods)

    for i in range(n):
        if check_vip(periods[i], sum(payments[i])) == True:
            if check_vip(periods[i]+1, sum(payments[i][1:]) + estimates[i]) == False:
                answer[1] += 1

        if check_vip(periods[i], sum(payments[i])) == False:
            if check_vip(periods[i]+1, sum(payments[i][1:]) + estimates[i]) == True:
                answer[0] += 1


    return answer

pe1 = [20, 23, 24]
py1 = [[
        100000, 100000, 100000, 100000, 100000, 100000,
        100000, 100000, 100000, 100000, 100000, 100000
    ],
    [
        100000, 100000, 100000, 100000, 100000, 100000,
        100000, 100000, 100000, 100000, 100000, 100000
    ],
    [
        350000, 50000, 50000, 50000, 50000, 50000,
        50000, 50000, 50000, 50000, 50000, 50000
    ]
]
es1 = [100000, 100000, 100000]

# pe2 =
# py2 =
# es2 =

print(solution(pe1, py1, es1))
# print(solution(pe2, py2, es2))