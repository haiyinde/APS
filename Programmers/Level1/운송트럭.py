def solution(max_weight: int, specs: list, names: list):
    answer = 1
    cur_sum = 0
    spec_dict = {spec[0]: int(spec[1]) for spec in specs}

    for name in names:
        weight = spec_dict[name]
        if cur_sum + weight > max_weight:
            answer += 1
            cur_sum = 0
        cur_sum += weight

    # pop(0)으로 하면 시간초과나서 for문으로 교체함
    return answer