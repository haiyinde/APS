def solution(s):
    length = []
    result = ""
    if len(s) == 1:
        return 1

    for cut in range(1, len(s) // 2 + 1):
        count = 1  # 기본 반복값 1
        tmp = s[:cut]  # 다음 문자열과 비교
        for nxt in range(cut, len(s), cut):  # 자른 다음 문자열부터, 끝까지, 자른 길이만큼 반복해서 보기
            if s[nxt:nxt + cut] == tmp:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tmp
                tmp = s[nxt:nxt + cut]
                count = 1
        if count == 1:
            count = ""
        result += str(count) + tmp
        length.append(len(result))
        result = ""

    return min(length)