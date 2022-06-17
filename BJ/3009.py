coordinates_x: dict = dict()
coordinates_y: dict = dict()

for _ in range(3):
    x, y = map(int, input().split())
    if x in coordinates_x:
        coordinates_x[x] += 1
    else:
        coordinates_x[x] = 1
    if y in coordinates_y:
        coordinates_y[y] += 1
    else:
        coordinates_y[y] = 1

for k, v in coordinates_x.items():
    if v == 1:
        print(k, end=" ")

for k, v in coordinates_y.items():
    if v == 1:
        print(k)