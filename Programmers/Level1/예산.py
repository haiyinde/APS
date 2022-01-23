def solution(d, budget):
    d = sorted(d)

    answer = 0
    while d:
        turn = d.pop(0)
        if budget < turn:
            break
        budget -= turn
        answer += 1

    return answer