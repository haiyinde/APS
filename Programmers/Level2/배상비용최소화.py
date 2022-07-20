# 시간복잡도 : O(n log n)
from heapq import heapify, heapreplace

def solution(no: int, works: list):
    if sum(works) < no:
        return 0

    # maxheap
    # works = [-i for i in works]
    for i in range(len(works)):  # O(n)
        works[i] = -1 * works[i]
    heapify(works)


    for _ in range(no):  # no만큼 반복하면 while보다는 for를 사용하자
        heapreplace(works, works[0]+1)  # 피드백 : heappop과 heappush가 연달아 나오면 heapreplace를 써도 된다.

    # while no > 0:
    #     biggest = heappop(works)  # O(log n)
    #     biggest += 1
    #     heappush(works, biggest)  # O(log n)
    #     no -= 1

    # comprehension을 이용하자
    return sum(work ** 2 for work in works)
    # result = 0
    # for i in range(len(works)):  # O(n)
    #     result += works[i] ** 2
    #
    # # O(n log n)
    # return result