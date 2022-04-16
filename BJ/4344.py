C = int(input())
for _ in range(C):
    lst = list(map(int, input().split()))
    N = lst[0]
    scores = lst[1:]
    avg = sum(scores)/N
    count = 0
    for score in scores:
        if score > avg:
            count += 1
    print("{:.3f}% ".format(round(count/N*100, 3)))