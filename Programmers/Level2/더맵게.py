# 파이썬의 경우 LBYL 보다 EAFP 예외 처리를 권장한다.
# EAFP : Easier to Ask Forgiveness than Permission  => try except
# LBYL : Look Before You Leap => if else

from heapq import heapify, heappop, heappush

def solution(scoville, K):
    answer = 0
    heapify(scoville)

    while scoville[0] < K:
        try:
            heappush(scoville, heappop(scoville) + heappop(scoville) * 2)
            answer += 1
        except:
            return -1

    return answer

# from heapq import heapify, heappush, heappop
#
# def solution(scoville, K):
#     # 입력: 백만이하 => 백만 이하일 경우 : 최대O(nlogn)
#     answer = 0
#     heapify(scoville)
#     # minheap, 루트노드가 K이상
#     while scoville[0] < K:
#         if len(scoville) == 1:
#             return -1
#         least_hot = heappop(scoville)  # O(log n)
#         scnd_least_hot = heappop(scoville) # O(log n)
#         mixed = least_hot + scnd_least_hot * 2
#         heappush(scoville, mixed) # O(log n)
#         answer += 1
#
#     # 시간복잡도 O(nlogn)?
#     return answer

# import heapq

# def solution(scoville, K):
#     scoville.sort()

#     answer = 0

#     while scoville[0] <= K:
#         try:
#             f1 = heapq.heappop(scoville)
#             f2 = heapq.heappop(scoville)
#             heapq.heappush(scoville, f1 + f2 * 2)
#         except:
#             return -1
#         answer += 1

#     return answer

# 시간 초과 ㅡㅡ
def solution(scoville, K):
    answer = 0
    front = 0

    while scoville[front] <= K:
        scoville.sort()
        f1 = scoville[front]
        f2 = scoville[front + 1]
        new_food = f1 + f2 * 2
        answer += 1
        front += 2
        scoville.append(new_food)

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
