# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    result = float('INF')
    for i in range(len(A)-K+1):
        temp = list(A)
        del temp[i:i+K]
        temp_am = max(temp) - min(temp)
        if temp_am < result:
            result = temp_am
    return result
print(solution([5, 3, 6, 1, 3], 2))