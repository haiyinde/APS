def solution(n, lost, reserve):
    answer = n - len(lost)
    for ls in lost:
        if ls-1 in reserve:
            reserve.remove(ls-1)
            answer += 1
        elif ls+1 in reserve:
            reserve.remove(ls+1)
            answer += 1
    return answer

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))