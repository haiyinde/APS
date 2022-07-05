import math

def solution(progresses: list, speeds: list):
    # 입력 100 이하: 최대 O(n^3) => 완전탐색, 백트래킹
    # 무조건 입력의 갯수로 판단하는 것은 함정일 수 있기 때문에 무조건 따르지는 않기!
    answer = []
    days = []

    for p, s in zip(progresses, speeds):
        left = 100 - p
        done = math.ceil(left / s)
        days.append(done)

    release_date = 0
    for day in days:
        if day > release_date:
            release_date = day
            answer.append(1)
        else:
            answer[-1] += 1

    # Queue나 heap 미사용
    # 시간복잡도 : O(n)
    return answer