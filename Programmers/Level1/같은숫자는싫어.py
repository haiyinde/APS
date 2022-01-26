def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(len(arr)):
        num = arr[i]
        if num != answer[-1]:
            answer.append(num)
    return answer