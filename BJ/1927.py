import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N: int = int(input())  # 입력 제한 100만이하 O(n log n) => 힙, 우선순위 큐 & 정렬 & DP & 위상정렬 & 다익스트라
lst: list = list()

for _ in range(N):
    x = int(input())
    if x > 0:
        heappush(lst, x)  # O(log n)
    else:
        if len(lst) == 0:
            print(0)
        else:
            print(heappop(lst))  # O(log n)

# 추정 Big-O : O(2logn)
