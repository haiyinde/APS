# N개의 통나무
# 통나무의 높이 차가 최소
# 최소 난이도를 출력하라
# 2 5 9 7 4  -> 4

import sys
input = sys.stdin.readline

# 가장 큰 통나무를 중간에 세운다.

T = int(input())
for _ in range(T):
    N = int(input())  # 통나무의 개수를 나타내는 정수 N
    Li = list(map(int, input().split()))
    Li = sorted(Li)

    arranged = []  # 통나무 놓기
    if N%2:  # 홀수
        for i in range(0, N, 2):
            arranged.append(Li[i])
        for i in range(N-2, 0, -2):
            arranged.append(Li[i])
    else:  # 짝수
        for i in range(0, N, 2):
            arranged.append(Li[i])
        for i in range(N-1, 0, -2):
            arranged.append(Li[i])

    # 첫번째와 마지막 통나무 높이차와 나머지 통나무들간의 높이차 비교
    result = abs(arranged[0]-arranged[-1])
    for i in range(N-1):
        result = max(result, abs(arranged[i]-arranged[i+1]))

    print(result)

# 의문점 : sort()로 했을때는 3번째 예시 테스트케이스에서 오류
# sorted()로 하면 잘 통과가 된다 .. 왜일까






