def solution(strings, n):
    answer = sorted(sorted(strings), key=lambda strings: strings[n])

    print(answer)
    return answer