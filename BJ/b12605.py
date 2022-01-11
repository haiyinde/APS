N = int(input())

for test_case in range(1, N+1):
    L = list(input().split())

    result = ''
    for i in range(len(L)-1, -1, -1):
        result += L[i] + ' '

    print('Case #{}: {}'.format(test_case, "".join(result)))
