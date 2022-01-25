def solution(n):
    watermelon = '수박'*n
    print(watermelon)
    answer = ''
    for i in range(n):
        answer += watermelon[i]
    return answer

# 더 효율적인 풀이
def solution(n):
    watermelon = '수박'*(n//2+1)
    return watermelon[:n]