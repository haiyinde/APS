def solution(n):
    if n <= 3:
        return '124'[n - 1]
    else:
        tmp1 = (n - 1) // 3
        tmp2 = (n - 1) % 3
        return solution(tmp1) + '124'[tmp2]

    return answer 
