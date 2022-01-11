def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    winner = []

    o1 = 0
    o2 = 0
    o3 = 0
    for i in range(len(answers)):
        now = answers[i]
        c1 = i % 5
        c2 = i % 8
        c3 = i % 10

        if now == student1[c1]:
            o1 += 1
        if now == student2[c2]:
            o2 += 1
        if now == student3[c3]:
            o3 += 1

    highest_score = max(o1, o2, o3)

    if highest_score == o1:
        winner.append(1)
    if highest_score == o2:
        winner.append(2)
    if highest_score == o3:
        winner.append(3)

    return winner