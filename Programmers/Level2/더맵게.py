import heapq


def solution(scoville, K):
    scoville.sort()

    answer = 0

    while scoville[0] <= K:
        try:
            f1 = heapq.heappop(scoville)
            f2 = heapq.heappop(scoville)
            heapq.heappush(scoville, f1 + f2 * 2)
        except:
            return -1
        answer += 1

    return answer

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