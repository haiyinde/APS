T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    milky_way_map = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for planet in milky_way_map:
        cx, cy, r = planet[0], planet[1], planet[2]
        start_length = ((x1-cx)**2 + (y1-cy)**2)**0.5
        finish_length = ((x2-cx)**2 + (y2-cy)**2)**0.5
        if start_length < r and finish_length < r:  # 출발점과 도착점에서 각각 행성 중심과의 거리가 행성 반지름보다 작은 경우
            continue
        elif start_length < r:
            result += 1
        elif finish_length < r:
            result += 1
    print(result)