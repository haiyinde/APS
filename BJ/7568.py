N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]

for i in people:
    rank = 1
    for j in people:
        if not (i == j):
            if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end=" ")
