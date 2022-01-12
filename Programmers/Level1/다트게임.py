def solution(dartResult):
    n = ''
    score = []
    bonuses = {'S': 1, 'D': 2, 'T': 3}
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i in bonuses:
            n = int(n)**bonuses[i]
            score.append(n)
            n = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif i == '#':
            score[-1] = score[-1] * -1
        
    return sum(score)