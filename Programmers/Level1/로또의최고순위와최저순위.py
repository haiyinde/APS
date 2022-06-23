def solution(lottos, win_nums):
    answer = [0, 0]

    highest = 0
    lowest = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            lowest += 1
        elif lottos[i] == 0:
            highest += 1

    rank_dict: dict = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    answer[0] = rank_dict[highest + lowest]
    answer[1] = rank_dict[lowest]

    return answer