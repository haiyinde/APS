N: int = int(input())
coordinates: list = list(map(int, input().split()))
temp: list = sorted(list(set(coordinates)))

index: dict = dict()
for i in range(len(temp)):
    index[temp[i]] = i

for i in coordinates:
    print(index[i], end=" ")