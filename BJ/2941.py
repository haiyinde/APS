Croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

S = input()
result = len(S)  # result의 최대치는 문자열의 길이
# 최대 길이 - 크로아티안 알파벳을 발견했다면 중복된 알파벳 수를 빼주는 방식으로 구현
for i in range(1, len(S)):  # 뒷 글자를 기준으로 잡았으므로 0이 아닌 1부터 탐색하여 index Error 방지
    # 크로아티아 알파벳을 '='이 포함된 것, '-'이 포함된 것, 'j'가 포함된 것 세 개로 나누어 주었다.
    # c= c- dz= s= z= 검사
    if S[i] == '=':
        # dz= 검사를 먼저 한다.
        if i >= 2 and S[i-1] == 'z' and S[i-2] == 'd':
            result -= 2
        # z= 검사 순서를 늦게 해서 dz=일때 먼저 2개를 빼고 지나가도록
        elif S[i-1] == 'c' or S[i-1] == 's' or S[i-1] == 'z':
            result -= 1
    # c- d- 검사
    elif S[i] == '-':
        if S[i-1] == 'c' or S[i-1] == 'd':
            result -= 1
    # lj nj 검사
    elif S[i] == 'j':
        if S[i-1] == 'l' or S[i-1] == 'n':
            result -= 1

print(result)