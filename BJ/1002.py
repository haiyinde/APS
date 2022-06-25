T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    length = ((x2-x1)**2 + (y2-y1)**2) ** 0.5

    # 두 원의 중심이 같을 경우
    if x1 == x2 and y1 == y2:
        # 두 원이 겹치는 경우, 접점이 무수히 많다
        if r1 == r2:
            print(-1)
        # 동심원
        else:
            print(0)
    # 두 원의 중심이 다를 경우
    else:
        # 외접원 or 내접원
        if length == r1 + r2 or length == abs(r2-r1):
            print(1)
        elif length < r1 + r2 and length > abs(r2-r1):
            print(2)
        else:
            print(0)