#비트 우정지수
T = int(input())
for i in range(T):
    N, M = map(str, input().split()) # 두 이진수 str으로 받기
    count = [0] * 3

    for bit in range(len(N)):
        if N[bit] != M[bit]:
            count[0] += 1
            if N[bit] == '1':
                count[1] += 1
            else:
                count[2] += 1

    print(count[0] - min(count[1], count[2]))






