def solution(n, m):
    answer = []
    for i in range(n, 0, -1):
        if m % i == 0 and n % i == 0:  # 최대공약수
            answer.append(i)
            break
    answer.append(answer[0] * (n // answer[0]) * (m // answer[0]))
    return answer

print(solution(3, 12))
print(solution(2, 5))