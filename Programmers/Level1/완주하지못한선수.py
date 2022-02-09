import collections

def solution(participant, completion):
    participant.sort()
    completion.sort()

    answer = list(collections.Counter(participant) - collections.Counter(completion))[0]
    print(answer)

    return answer