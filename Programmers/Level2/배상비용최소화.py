from heapq import heapify, heappush, heappop

def solution(no: int, works: list):
    if sum(works) < no:
        return 0

    # maxheap
    for i in range(len(works)):  # O(n)
        works[i] = -1 * works[i]
    heapify(works)

    while no > 0:
        biggest = heappop(works)  # O(log n)
        biggest += 1
        heappush(works, biggest)  # O(log n)
        no -= 1

    result = 0
    for i in range(len(works)):  # O(n)
        result += works[i] ** 2

    # O(n log n) ??
    return result