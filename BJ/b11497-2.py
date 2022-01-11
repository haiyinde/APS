# 버블정렬 연습해보려고 했는데 백준에서는 시간초과남 '-' 너무해라..
import sys
input = sys.stdin.readline


def bubble_sort(a):
    for i in range(len(a)-1, 0, -1):  # 뒤에서부터 정렬, 맨앞은 자동정렬되어서 포함X
        for j in range(i):
            if a[j] > a[j+1]: # 만약 앞의 값이 더 크면
                a[j], a[j+1] = a[j+1], a[j]

    return a


T = int(input())
for _ in range(T):
    N = int(input())  # 통나무의 개수를 나타내는 정수 N
    Li = list(map(int, input().split()))

    # Li = sorted(Li)   # sorted()를 사용하지 말고 정렬해보자!
    Li = bubble_sort(Li)

    arranged = []  # 통나무 놓기
    if N%2:  # 홀수
        for i in range(0, N, 2):
            arranged.append(Li[i])
        for i in range(N-2, 0, -2):
            arranged.append(Li[i])
    else:  # 짝수
        for i in range(0, N, 2):
            arranged.append(Li[i])
        for i in range(N-1, 0, -2):
            arranged.append(Li[i])

    # 첫번째와 마지막 통나무 높이차와 나머지 통나무들간의 높이차 비교
    result = abs(arranged[0]-arranged[-1])
    for i in range(N-1):
        result = max(result, abs(arranged[i]-arranged[i+1]))

    print(result)






