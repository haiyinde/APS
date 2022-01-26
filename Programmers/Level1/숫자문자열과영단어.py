def solution(s):
    dictionary = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    answer = ''
    tmp = ''
    for p in s:
        if p.isdecimal():
            answer += p
        else:
            tmp += p
            if tmp in dictionary:
                answer += dictionary[tmp]
                tmp = ''

    return int(answer)