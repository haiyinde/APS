from heapq import heappush, heappop, heapify
from collections import deque


def solution(healths: list, items: list):
    answer = []
    healths = sorted(healths)
    items = deque(sorted([item[1], item[0], index + 1] for index, item in enumerate(items)))
    print(items)
    possible_strength = list()

    for health in healths:
        while items:
            debuff, buff, index = items[0]
            # print(debuff, buff, index)
            if health - debuff >= 100:
                items.popleft()
                heappush(possible_strength, [-buff, index])
            else:
                break

        if possible_strength:
            _, index = heappop(possible_strength)
            answer.append(index)

    return sorted(answer)