import operator
import math

# 개발에 필요한 days를 미리 계산 => 가장 오래 걸린 days를 저장 후 append 하는 방식
def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    done = [100] * N   # 개발 진행도 100인 리스트 만들기
    left = list(map(operator.sub, done, progresses))
    # map(operator.sub, A, B) = A리스트의 element - B리스트의 element
    # left === 남은 진행사항을 담은 리스트
    # 예시1의 left = [7, 70, 45]
    left_days = list(map(operator.truediv, left, speeds))
    # map(operator.truediv, A, B) = A리스트의 element / B리스트의 element
    # left_days === 남은 진행사항 / 진행 속도 => 작업이 끝나기까지 남은 일수
    # 예시1의 left_days = [7, 2.xx, 9]
    ceiled_left_days = list(map(math.ceil, left_days))
    # math.ceil === 올림처리
    # 예시1의 ceiled_left_days = [7, 3, 9] => 각 기능이 왼료되는 날
    front = 0
    # 가장 오래 걸린 days를 저장하는 인덱스
    for idx in range(N):
        if ceiled_left_days[idx] > ceiled_left_days[front]:
            answer.append(idx - front)
            front = idx
    answer.append(N - front)
    # idx = 0, front = 0 => 7 > 7: if문 X
    # idx = 1, front = 0 => 3 > 7: if문 X
    # idx = 2, front = 0 => 9 > 7: if문 탐색 => 앞에 있는 progress들을 answer에 append
    # 가장 오래 걸린 날을 front에 저장
    # N-front => for문을 다 돌고 남은 모든 날(N) - 가장 오래 걸린 날(front) 마지막날 배포하는 기능들

    return answer