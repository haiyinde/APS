N: int = int(input())
coordinates: list = [list(map(int, input().split())) for _ in range(N)]

coordinates.sort(key=lambda x: (x[1], x[0]))

for c in coordinates:
    print(*c)