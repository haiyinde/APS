def solution(array, commands):
    answer = []
    for c in range(len(commands)):
        i, j, k = commands[c][0], commands[c][1], commands[c][2]
        cut = array[i-1:j]
        srtd_array = sorted(cut)
        answer.append(srtd_array[k-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))