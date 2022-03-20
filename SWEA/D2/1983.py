# D2
import sys
sys.stdin = open("input.txt", "r")

result = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(N)]
    grades = [0] * len(scores)
    for i in range(len(scores)):
        grades[i] = scores[i][0] * 0.35 + scores[i][1] * 0.45 + scores[i][2] * 0.2
    kth_score = grades[K-1]
    # 앞에서 kth_score 변수 선언을 통해 값을 담아주고 sort를 해야 처음에 받았던 값의 kth를 받을 수 있는데
    # 그렇게 안하고 출력할 때 grades[K-1]을 해서 sorted된 값에서 K번째 성적의 등급을 출력해서 오답이 났었음
    grades = sorted(grades, reverse=True)
    d = N // 10
    print("#{} {}".format(t, result[grades.index(kth_score)//d]))
