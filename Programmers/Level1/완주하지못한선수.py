def solution(participant, completion):
    answer = ''
    while len(participant) == 1:
        c = completion[0]
        if c in participant:
            participant.remove(c)

    answer = participant[0]

    return answer

# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))