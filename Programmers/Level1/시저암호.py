def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
            continue
        pushed_num = ord(i) + n
        if pushed_num > 90 and 65 <= ord(i) <= 90:  #대문자인데 대문자를 넘어갔다면
            pushed_num -= 26
        elif pushed_num > 122:
            pushed_num -= 26
        answer += chr(pushed_num)
    return answer