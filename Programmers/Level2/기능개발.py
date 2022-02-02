import operator
import math


def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    done = [100] * N
    left = list(map(operator.sub, done, progresses))
    left_days = list(map(operator.truediv, left, speeds))
    ceiled_left_days = list(map(math.ceil, left_days))
    print(ceiled_left_days)
    front = 0

    for idx in range(N):
        if ceiled_left_days[idx] > ceiled_left_days[front]:
            answer.append(idx - front)
            front = idx
    answer.append(N - front)

    return answer